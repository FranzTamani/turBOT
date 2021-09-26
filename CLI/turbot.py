#!/usr/bin/python3

import os
import sys
import subprocess
import itertools
import threading
import time
import argparse

# Error code to return on exception
EXCEPTION_ERROR_CODE = 1

# Terminal colours:
WARNING = '\033[93m'
ERROR = '\033[91m'
NO_COLOUR = '\x1b[0m'

# Inject modes:
INJECT_MODES = ["lazy","no_call"]

done = False

def progress(message):
    global done
    done = False
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r' + message + ' ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     \n')

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Disassemble, Assmeble and Obfuscate are similar atm for demo purposes.
# They will be moved to modules later on as they will get complex once integrated with their corresponding tools
def disassemble(source_dir, output_dir):
    try:
        if os.path.isfile(source_dir):
            print("Program is currently disassembling")
        else:
            print(f"{ERROR}ERROR: Disassembly target file not found{NO_COLOUR}")
            return 2

        args = ["ddisasm", source_dir, "--asm", output_dir] # Console Commands Go Here, split strings
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        p.wait() # Wait for subprocess to finish executing
        exit_code = p.poll()
        # Return exit code to know if to proceed
        return exit_code

    except Exception as e:
        print(e)
        print(f"{ERROR}An error occured during the decompilation proccess{NO_COLOUR}")
        # Return exception error code
        return EXCEPTION_ERROR_CODE

# Disassemble, Assmeble and Obfuscate are similar atm for demo purposes.
# They will be moved to modules later on as they will get complex once integrated with their corresponding tools
def reassemble(source_dir, output_dir): 
    try:
        if os.path.isfile(source_dir):
            print("Program is currently reassembling")
        else:
            print(f"{ERROR}ERROR: Reassembly target file not found{NO_COLOUR}")
            return 2
        
        args = ["g++", "-pthread", "-no-pie", "-o", output_dir, source_dir] # Console Commands Go Here, split strings
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        p.wait() # Wait for subprocess to finish executing
        exit_code = p.poll()
        # Return exit code to know if to proceed
        return exit_code
        
    except Exception as e:
        print(e)
        print(f"{ERROR}An error occured during the compilation proccess{NO_COLOUR}")
        # Return exception error code
        return EXCEPTION_ERROR_CODE    

# Disassemble, Assmeble and Obfuscate are similar atm for demo purposes.
# They will be moved to modules later on as they will get complex once integrated with their corresponding tools
def obfuscate(source_dir, output_dir, inject_mode, inject_files): 
    if not inject_files:
        print(f'{ERROR}ERROR: At least one payload must be supplied if using -O or -A {NO_COLOUR}\nSupply payloads in the form: -p payload_path [-p payload_path [...]]')
        return 22
    try:
        if os.path.isfile(source_dir):
            print("Program is currently obfuscating the assembly file")
        else:
            print(f"{ERROR}ERROR: Obfuscation target file not found{NO_COLOUR}")
            return 2
        
        invalid_files = []
        for f in inject_files:
            if not os.path.isfile(f):
                print(f"{WARNING}WARNING: {f}: file not found. This payload will not be used in the obfuscation process{NO_COLOUR}")
                invalid_files.append(f)
        inject_files = [f for f in inject_files if f not in invalid_files]
        if not inject_files:
            print(f"{ERROR}ERROR: no payload files were found. Obfuscation cannot proceed{NO_COLOUR}")
            return 2

        # Set up sed parameters:
        if inject_mode=="lazy":
            call_start = "/main:/a "
        elif inject_mode=="no_call":
            call_start = "/ret/a "
        else:
            # Unhandled inject mode
            return EXCEPTION_ERROR_CODE 
        file_inject_params = []
        for i in range(len(inject_files)):
            method_name = parse_filename(inject_files[i])
            call_line = call_start + f"call {method_name}"
            file_inject_params += ["-e", "3r " + inject_files[i], "-e", call_line]
        args = ["sed"] + file_inject_params + [source_dir] # Console Commands Go Here, split strings
        with open(output_dir, "w") as output_file:
            p = subprocess.Popen(args, stdout=output_file)
            p.wait() # Wait for subprocess to finish executing
            exit_code = p.poll()
        # Return exit code to know if to proceed
        return exit_code
        
    except Exception as e:
        print(e)
        print(f"{ERROR}An error occured during the obfuscation proccess{NO_COLOUR}")
        # Return exception error code
        return EXCEPTION_ERROR_CODE

# Returns the filename prefix
# Expected input /path/to/directory/filename_prefix.extension
# Returns filename_prefix
def parse_filename(file_path):
    filename = file_path.split('/')[-1]
    prefix = filename.split('.')[0]
    return prefix
        
def main():
    parser = argparse.ArgumentParser(description='Binary Obfuscation Tool (BOT)')
    parser.add_argument('-A', action='store_const', const=True, default=False, help='Performs disassembly, obfuscation and reassembly to a given binary'
                            'This requires a filename prefix for the destination arguement if the destination argument is specified')
    parser.add_argument('-D', action='store_const', const=True, default=False, help='Disassembles a specified binary')
    parser.add_argument('-R', action='store_const', const=True, default=False, help='Reassembles a specified assembly file')
    parser.add_argument('-O', action='store_const', const=True, default=False, help='Obfuscates a specified assembly file')
    parser.add_argument('-p', "--payload", action='append', help='Optional: Paths to .s files to be used for obfuscation mode as payloads. This flag can be used multiple times'
                            ' to specify multiple payloads to add. These files must be named for the function to be called inside them. i.e. [func_name].s', metavar='payload', dest='payloads')
    parser.add_argument('-m', '--mode', action='store', default='lazy', choices=INJECT_MODES, help='Optional: The obfuscation mode. Ignored if -O is not present.\n(default: %(default)s)', dest='mode')
    parser.add_argument('source', nargs='?', default='', metavar='source', type=str, help='The dir where the file is located source/path/file.ext')
    parser.add_argument('destination', nargs='?', default=os.getcwd(), metavar='destination', type=str, help='Optional: The dir where the output file will be stored "/output/path/filename-prefix.ext"' 
                            'When "-A" flag is set file extensions are auto generated')

    args = parser.parse_args(sys.argv[1:]) # Ignores the initial sys.argv which contains the path to this script
    print(os.getcwd())
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Set the base file name for use when destination is not specified
    filename = parse_filename(args.source)

    if args.A or (args.D and args.R and args.O):     # Step through all commands (happens if all false or all true)
        print('Running all commands')

        if os.path.isdir(args.destination):
            dis_dest = os.path.join(args.destination, f'{filename}-disassembled.s')
            obf_dest = os.path.join(args.destination, f'{filename}-obfuscated.s')
            rea_dest = os.path.join(args.destination, f'{filename}-reassembled.out')
        else:
            filename = parse_filename(args.destination)
            dis_dest = os.path.join(args.destination, f'{filename}-disassembled.s')
            obf_dest = os.path.join(args.destination, f'{filename}-obfuscated.s')
            rea_dest = os.path.join(args.destination, f'{filename}-reassembled.out')

        exit_code = disassemble(args.source, dis_dest)
        if exit_code:
            print(f"{ERROR}Error encountered during disassembly. Halting...{NO_COLOUR}")
            sys.exit(exit_code)
        exit_code = obfuscate(dis_dest, obf_dest, args.mode, args.payloads)
        if exit_code:
            print(f"{ERROR}Error encountered during obfuscation. Halting...{NO_COLOUR}")
            sys.exit(exit_code)
        exit_code = reassemble(obf_dest, rea_dest)
        if exit_code:
            print(f"{ERROR}Error encountered during resassembly. Halting...{NO_COLOUR}")
            sys.exit(exit_code)
        sys.exit(0)

    elif args.D:                        # Disassembles given binary
        print('Running Disassemble Only')
        if args.destination == os.getcwd():
            dis_dest = os.path.join(args.destination, f'{filename}-disassembled.s')
        else:
            dis_dest = args.destination
        disassemble(args.source, dis_dest)

    elif args.O:                        # Obfuscates given assembly file
        print('Running Obfuscate Only')
        if args.destination == os.getcwd():
            obf_dest = os.path.join(args.destination, f'{filename}-obfuscated.s')
        else:
            obf_dest = args.destination
        obfuscate(args.source, obf_dest, args.mode, args.payloads)

    elif args.R:                        # Reassembles given assembly file into an executable binary
        print('Running Reassemble Only')
        if args.destination == os.getcwd():
            rea_dest = os.path.join(args.destination, f'{filename}-reassembled.out')
        else:
            rea_dest = args.destination
        reassemble(args.source, rea_dest)

    else:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
main()
