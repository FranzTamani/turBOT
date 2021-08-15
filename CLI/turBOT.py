#!/usr/bin/python3

import os
import sys
import subprocess
import itertools
import threading
import time
import argparse
# from os.path import dirname, basename, isfile, join
# import glob
# modules = glob.glob(join(dirname(__file__), "*.py"))
# __all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

done = False

def progress(message):
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
        t = threading.Thread(target=progress, args=(message,))
        t.start()
        # p = subprocess.Popen(["<Path to Decompiler>", "<Disassemble Command>", source_dir, output_dir]) TODO: HOW DO WE ACTUALLY DISASSEMBLE STUFF??
        time.sleep(5)
        # p.wait() # Wait for subprocess to finish executin
        # Condition Variable for "Loading" process
        global done
        done = True

        t.join()

        # TODO: GET RID OF THIS SECTION ONCE WE HAVE DISASSEMBLY ACTUALLY WORKING
        with open(output_dir, 'w') as fp:
            fp.write("This is a sample File")
        
        print(source_dir + " has been disassembled to " + output_dir)
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
        t = threading.Thread(target=progress, args=(message,))
        t.start()
        # p = subprocess.Popen(["<Path to Compiler>", "<Assmeble Command>", source_dir, output_dir]) TODO: HOW DO WE ACTUALLY COMPILE STUFF??
        time.sleep(5)
        # p.wait() # Wait for subprocess to finish executin
        # Condition Variable for "Loading" process
        global done
        done = True

        t.join()

        # TODO: GET RID OF THIS SECTION ONCE WE HAVE DECOMPILATION ACTUALLY WORKING
        with open(output_dir, 'w') as fp:
            fp.write("This is a sample File")
        
        print(source_dir + " has been compiled to " + output_dir)
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
        t = threading.Thread(target=progress, args=(message,))
        t.start()
        # p = subprocess.Popen(["<Path to Obfuscator>", "<Obfuscator Command>", source_dir, output_dir]) TODO: HOW DO WE ACTUALLY OBFUSCATE STUFF??
        time.sleep(5)
        # p.wait() # Wait for subprocess to finish executin
        # Condition Variable for "Loading" process
        global done
        done = True

        t.join()

        # TODO: GET RID OF THIS SECTION ONCE WE HAVE DECOMPILATION ACTUALLY WORKING
        with open(output_dir, 'w') as fp:
            fp.write("This is a sample File")
        
        print(source_dir + " has been compiled to " + output_dir)
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
    parser = argparse.ArgumentParser(description='Binary Obfuscation Tool (BOT), default flags -DRO')
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
