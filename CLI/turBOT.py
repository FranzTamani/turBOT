import os
import sys
import subprocess
import itertools
import threading
import time
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

def help():
    help_output = """
    \rThis is the help command, put command definitions here!
    """
    print(help_output)

# Decompile, Compile and Obfuscate are similar atm for demo purposes.
# They will be moved to modules later on as they will get complex once integrated with their corresponding tools
def decompile(source_dir, output_dir):
    try:
        if os.path.isfile(source_dir):
            print("File found")
        message = "Program is currently decompiling"
        t = threading.Thread(target=progress, args=(message,))
        t.start()
        # p = subprocess.Popen(["<Path to Decompiler>", "<Decompile Command>", source_dir, output_dir]) TODO: HOW DO WE ACTUALLY DECOMPILE STUFF??
        time.sleep(5)
        p.wait() # Wait for subprocess to finish executin
        # Condition Variable for "Loading" process
        global done
        done = True

        t.join()

        # TODO: GET RID OF THIS SECTION ONCE WE HAVE DECOMPILATION ACTUALLY WORKING
        with open(output_dir, 'w') as fp:
            fp.write("This is a sample File")
        
        print(source_dir + " has been decompiled to " + output_dir)
    except Exception as e:
        print(e)
        print("An error occured during the decompilation proccess")

# Decompile, Compile and Obfuscate are similar atm for demo purposes.
# They will be moved to modules later on as they will get complex once integrated with their corresponding tools
def compile(source_dir, output_dir): 
    try:
        if os.path.isfile(source_dir):
            print("File found")
        message = "Program is currently compiling"
        t = threading.Thread(target=progress, args=(message,))
        t.start()
        # p = subprocess.Popen(["<Path to Compiler>", "<Compile Command>", source_dir, output_dir]) TODO: HOW DO WE ACTUALLY COMPILE STUFF??
        time.sleep(5)
        p.wait() # Wait for subprocess to finish executin
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

# Decompile, Compile and Obfuscate are similar atm for demo purposes.
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
        p.wait() # Wait for subprocess to finish executin
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

def main():
    # print(sys.argv)

    if len(sys.argv) > 4:
        print('You have specified too many arguments')
        sys.exit()

    elif len(sys.argv) <= 1:
        print('Please specify a command, type \'help\' to display all commabds')
        sys.exit()

    # Command Parsing... Did we want to make this OO or just leave it at functional?
    if sys.argv[1] == "help":
        help()
        sys.exit()
    elif sys.argv[1] == "decompile":
        if len(sys.argv) == 4:
            decompile(sys.argv[2], sys.argv[3])
        else:
            print('Usage: decompile "decompile/file/bin.o" "decompile/to/bin.asm"')
        sys.exit()
    elif sys.argv[1] == "compile":
        if len(sys.argv) == 4:
            compile(sys.argv[2], sys.argv[3])
        else:
            print('Usage: decompile "decompile/file/bin.asm" "decompile/to/bin.o"')
        sys.exit()
    elif sys.argv[1] == "obfuscate":
        if len(sys.argv) == 4:
            obfuscate(sys.argv[2], sys.argv[3])
        else:
            print('Usage: obfuscate "obfuscate/file/bin.asm" "obfuscate/to/bin.asm"')
        sys.exit()
    
    # if sys.argv
    
main()