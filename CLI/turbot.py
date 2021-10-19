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
INJECT_MODES = ["lazy","no_call","custom"]

done = False

def cleanup(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(f"The file {filename} does not exist")

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
            call_start = "/^main:/a "
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

def custom_obfuscate(source_dir, output_dir, script):
    if not script:
        print(f"{ERROR}ERROR: .sed script file must be supplied if using custom inject mode")
        return 22

    try:
        if os.path.isfile(source_dir):
            print("Program is currently obfuscating the assembly file")
        else:
            print(f"{ERROR}ERROR: Obfuscation target file not found{NO_COLOUR}")
            return 2
        
        with open(output_dir, "w") as output_file:
            p = subprocess.Popen(["sed", "-f", script, source_dir], stdout=output_file)
            p.wait()
            exit_code = p.poll()
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
    parser.add_argument('-s', '--script', action='store', help='Provide a .sed script for the custom inject mode to use. Required if inject mode is set to \'custom\', ignored otherwise', dest='script')
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

        if os.path.abspath(args.destination) == os.getcwd():
            dis_dest = os.path.join(args.destination, f'{filename}-disassembled.s')
            obf_dest = os.path.join(args.destination, f'{filename}-obfuscated.s')
            rea_dest = os.path.join(args.destination, f'{filename}-reassembled.out')
        else:
            dis_dest = f'{args.destination}-disassembled.s'
            obf_dest = f'{args.destination}-obfuscated.s'
            rea_dest = f'{args.destination}-reassembled.out'

        exit_code = disassemble(args.source, dis_dest)
        if exit_code != 0:
            print(f"{ERROR}Error encountered during disassembly. Halting...{NO_COLOUR}")
            sys.exit(exit_code)
        print(dis_dest)
        if args.mode == "custom":
            exit_code = custom_obfuscate(dis_dest, obf_dest, args.script)
        else:
            exit_code = obfuscate(dis_dest, obf_dest, args.mode, args.payloads)
        if exit_code != 0:
            print(f"{ERROR}Error encountered during obfuscation. Halting...{NO_COLOUR}")
            sys.exit(exit_code)
        print(obf_dest)
        exit_code = reassemble(obf_dest, rea_dest)
        if exit_code != 0:
            print(f"{ERROR}Error encountered during resassembly. Halting...{NO_COLOUR}")
            sys.exit(exit_code)
        cleanup(dis_dest)
        cleanup(obf_dest)
        sys.exit(0)

    # These will not run if -A or -DRO flags are set
    if args.D:                        # Disassembles given binary
        print('Running Disassemble Only')
        if args.destination == os.getcwd():
            dis_dest = os.path.join(args.destination, f'{filename}-disassembled.s')
        else:
            dis_dest = args.destination
        exit_code = disassemble(args.source, dis_dest)
        if exit_code != 0:
            print(f"{ERROR}Error encountered during disassembly. Halting...{NO_COLOUR}")
            sys.exit(exit_code)

    if args.O:                        # Obfuscates given assembly file
        print('Running Obfuscate Only')
        if os.path.abspath(args.destination) == os.getcwd():
            obf_dest = os.path.join(args.destination, f'{filename}-obfuscated.s')
        else:
            obf_dest = args.destination
        if args.D:
            target = dis_dest
        else:
            target = args.source

        if args.mode == "custom":
            exit_code = custom_obfuscate(target, obf_dest, args.script)
        else:
            exit_code = obfuscate(target, obf_dest, args.mode, args.payloads)

        if exit_code != 0:
            print(f"{ERROR}Error encountered during obfuscation. Halting...{NO_COLOUR}")
            sys.exit(exit_code)

    if args.R:                        # Reassembles given assembly file into an executable binary
        print('Running Reassemble Only')
        if args.destination == os.getcwd():
            rea_dest = os.path.join(args.destination, f'{filename}-reassembled.out')
        else:
            rea_dest = args.destination
        if args.D or args.O:
            if args.O:  # When file is obfuscated (means that it may have also been disassembled)
                exit_code = reassemble(obf_dest, rea_dest)
                cleanup(dis_dest)
                cleanup(obf_dest)
            else:       # Disassembled but not obfuscated
                exit_code = reassemble(dis_dest, rea_dest)
                cleanup(dis_dest)
        else:
            exit_code = reassemble(args.source, rea_dest)

        if exit_code != 0:
            print(f"{ERROR}Error encountered during obfuscation. Halting...{NO_COLOUR}")
            sys.exit(exit_code)

    if not (args.D or args.O or args.R):    # If none of the flags are set print error
        parser.print_help(sys.stderr)
        sys.exit(1)
    
main()
