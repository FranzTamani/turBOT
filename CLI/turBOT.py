#!/usr/bin/python3

import os
import sys
import subprocess
import itertools
import threading
import time
import argparse

# Error code to return on exception
EXCEPTION_ERROR_CODE = -1

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

# Disassemble, Assmeble and Obfuscate are similar atm for demo purposes.
# They will be moved to modules later on as they will get complex once integrated with their corresponding tools
def disassemble(source_dir, output_dir):
    try:
        if os.path.isfile(source_dir):
            print("Program is currently disassembling")
        else:
            print("Disassembly target file not found")
            return EXCEPTION_ERROR_CODE

        args = ["ddisasm", source_dir, "--asm", output_dir] # Console Commands Go Here, split strings
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        p.wait() # Wait for subprocess to finish executing
        exit_code = p.poll()
        # Return exit code to know if to proceed
        return exit_code

    except Exception as e:
        print(e)
        print("An error occured during the decompilation proccess")
        # Return exception error code
        return EXCEPTION_ERROR_CODE

# Disassemble, Assmeble and Obfuscate are similar atm for demo purposes.
# They will be moved to modules later on as they will get complex once integrated with their corresponding tools
def reassemble(source_dir, output_dir): 
    try:
        if os.path.isfile(source_dir):
            print("Program is currently reassembling")
        else:
            print("Reassembly target file not found")
            return EXCEPTION_ERROR_CODE
        
        args = ["g++", "-pthread", "-no-pie", "-o", output_dir, source_dir] # Console Commands Go Here, split strings
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        p.wait() # Wait for subprocess to finish executing
        exit_code = p.poll()
        # Return exit code to know if to proceed
        return exit_code
        
    except Exception as e:
        print(e)
        print("An error occured during the compilation proccess")
        # Return exception error code
        return EXCEPTION_ERROR_CODE    

# Disassemble, Assmeble and Obfuscate are similar atm for demo purposes.
# They will be moved to modules later on as they will get complex once integrated with their corresponding tools
def obfuscate(source_dir, output_dir, inject_mode = "LAZY", inject_files = ["HelloWorldInject.s"]): 
    try:
        if os.path.isfile(source_dir):
            print("Program is currently obfuscating the assembly file")
        else:
            print("Obfuscation target file not found")
            return EXCEPTION_ERROR_CODE

        # Set up sed parameters:
        if inject_mode=="LAZY":
            call_line = "/main:/a "
        elif inject_mode=="NO_CALL":
            call_line = "/ret/a "
        else:
            # Unhandled inject mode
            return EXCEPTION_ERROR_CODE 
        file_inject_params = []
        for i in range(len(inject_files)):
            method_name = parse_filename(inject_files[i])
            if i > 0:
                call_line += "\n "
            call_line += f"call {method_name} "
            file_inject_params += ["-e", "3r " + inject_files[i]]
        args = ["sed", "-e", call_line] + file_inject_params + [source_dir] # Console Commands Go Here, split strings
        output_file = open(output_dir, "w")
        p = subprocess.Popen(args, stdout=output_file)
        p.wait() # Wait for subprocess to finish executing
        exit_code = p.poll()
        output_file.close()
        # Return exit code to know if to proceed
        return exit_code
        
    except Exception as e:
        print(e)
        print("An error occured during the obfuscation proccess")
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
    parser = argparse.ArgumentParser(description='Binary Obfuscation Tool (BOT). The flags D, R and O are enabled by default')
    parser.add_argument('-D', action='store_const', const=True, default=False, help='Disassembles a specified binary')
    parser.add_argument('-R', action='store_const', const=True, default=False, help='Reassembles a specified assembly file')
    parser.add_argument('-O', action='store_const', const=True, default=False, help='Obfuscates a specified assembly file')
    parser.add_argument('source', metavar='F', type=str, help='The dir where the file is located source/path/file.ext')
    parser.add_argument('destination', metavar='T', type=str, help='The dir where the output file will be stored output/path/')
    # TODO: Add parameters to set obfuscation mode (default: LAZY) and to provide inject files for obfuscation

    args = parser.parse_args(sys.argv[1:]) # Ignores the initial sys.argv which contains the path to this script

    # Parses filename from source dir and prepare names for created outputs.
    filename = parse_filename(args.source)
    dis_dest = os.path.join(args.destination, f'{filename}-disassembled.s')
    obf_dest = os.path.join(args.destination, f'{filename}-obfuscated.s')
    rea_dest = os.path.join(args.destination, f'{filename}-reassembled.out')

    print(args)
    if args.D == args.R == args.O:     # Default behaviour, step through all commands (happens if all false or all true)
        print('Running default command')
        exit_code = disassemble(args.source, dis_dest)
        if exit_code:
            print("Error encountered during disassembly. Halting...")
            sys.exit(exit_code)
        exit_code = obfuscate(dis_dest, obf_dest)
        if exit_code:
            print("Error encountered during obfuscation. Halting...")
            sys.exit(exit_code)
        exit_code = reassemble(obf_dest, rea_dest)
        if exit_code:
            print("Error encountered during resassembly. Halting...")
            sys.exit(exit_code)
        sys.exit(0)

    elif args.D == True:                        # Disassembles given binary
        print('Running Disassemble Only')
        disassemble(args.source, dis_dest)

    elif args.O == True:                        # Obfuscates given assembly file
        print('Running Obfuscate Only')
        obfuscate(args.source, obf_dest)

    elif args.R == True:                        # Reassembles given assembly file into an executable binary
        print('Running Reassemble Only')
        reassemble(args.source, rea_dest)
    
main()
