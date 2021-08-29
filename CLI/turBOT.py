#!/usr/bin/python3

import os
import sys
import subprocess
import itertools
import threading
import time
import argparse

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
            print("File found")
        message = "Program is currently decompiling"

        args = ["ddisasm", "./empty.out", "--asm", "yeet.asm"] # Console Commands Go Here, split strings
        p = subprocess.Popen(args, stdout=subprocess.PIPE) # TODO: HOW DO WE ACTUALLY DISASSEMBLE STUFF??
        p.wait() # Wait for subprocess to finish executin
        exit_code = p.poll()
        print(f'Exit Code: {exit_code}')
        if exit_code == 0: # Command Exit Successfully
            print("Do Whatever")
        else: # Uh Oh Brokey
            print("Uh oh Brokey")
    except Exception as e:
        print(e)
        print("An error occured during the decompilation proccess")

# Disassemble, Assmeble and Obfuscate are similar atm for demo purposes.
# They will be moved to modules later on as they will get complex once integrated with their corresponding tools
def reassemble(source_dir, output_dir): 
    try:
        if os.path.isfile(source_dir):
            print("File found")
        message = "Program is currently compiling"
        
        args = [] # Console Commands Go Here, split strings
        p = subprocess.Popen(args, stdout=subprocess.PIPE) # TODO: HOW DO WE ACTUALLY DISASSEMBLE STUFF??
        p.wait() # Wait for subprocess to finish executin
        exit_code = p.poll()
        if exit_code == 0: # Command Exit Successfully
            print("Do Whatever")
        else: # Uh Oh Brokey
            print("Uh oh Brokey")
    except Exception as e:
        print(e)
        print("An error occured during the compilation proccess")        

# Disassemble, Assmeble and Obfuscate are similar atm for demo purposes.
# They will be moved to modules later on as they will get complex once integrated with their corresponding tools
def obfuscate(source_dir, output_dir): 
    try:
        if os.path.isfile(source_dir):
            print("File found")
        message = "Program is currently obfuscating the assembly file"

        args = [] # Console Commands Go Here, split strings
        p = subprocess.Popen(args, stdout=subprocess.PIPE) # TODO: HOW DO WE ACTUALLY DISASSEMBLE STUFF??
        p.wait() # Wait for subprocess to finish executin
        exit_code = p.poll()
        if exit_code == 0: # Command Exit Successfully
            print("Do Whatever")
        else: # Uh Oh Brokey
            print("Uh oh Brokey")
    except Exception as e:
        print(e)
        print("An error occured during the compilation proccess")   

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

    args = parser.parse_args(sys.argv[1:]) # Ignores the initial sys.argv which contains the path to this script

    # Parses filename from source dir and prepare names for created outputs.
    filename = parse_filename(args.source)
    dis_dest = args.destination + f'{filename}-disassembled.asm'
    obf_dest = args.destination + f'{filename}-obfuscated.asm'
    rea_dest = args.destination + f'{filename}-reassembled.o'

    print(args)
    if args.D == args.R == args.O == False or args.D == args.R == args.O == True:     # Default behaviour, step through all commands\
        print('Running default command')
        disassemble(args.source, dis_dest)
        obfuscate(dis_dest, obf_dest)
        reassemble(obf_dest, rea_dest)

    elif args.D == True:                        # Disassembles given binary
        print('Running Disassemble Only')
        disassemble(args.source, dis_dest)

    elif args.O == True:                        # Obfuscates given assembly file
        print('Running Obfuscate Only')
        obfuscate(dis_dest, obf_dest)

    elif args.R == True:                        # Reassembles given assembly file into an executable binary
        print('Running Reassemble Only')
        reassemble(obf_dest, rea_dest)
    
main()
