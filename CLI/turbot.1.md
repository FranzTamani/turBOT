---
title: turbot
section: 1
header: User Manual
footer: turbot 0.1.0
date: Oct 9, 2021
---

# NAME
turbot - Binary Obfuscation Tool

# SYNOPSIS
**turbot** [-h] [-A] [-D] [-R] [-O] [-p payload] [-m {lazy,no_call}] [source] [destination]

# DESCRIPTION
**turbot** (BOT or Binary Obfuscation Tool) is a CLI toolchain that allows users to add non-functional noise/payload to a Linux x86 ELF binary without breaking its functionality. The target audiences for this tool are cyber security researchers and developers.

# POSITIONAL ARGUMENTS
**source**
: The directory where the file to be disassembled/obuscated/reassembled is located ie. source/path/file.ext

**destination**          
: **Optional** The dir where the output file will be stored "/output/path/filename-prefix.ext  When"-A" flag is set file extensions are auto generated.

# Optional Arguements
**-h**, **--help**            
: Display help message

**-A**                    
: Perform disassembly, obfuscation and reassembly to a given binaryThis requires a filename prefix for the destination arguement if the destination argument specified

**-D**
: Disassembles a specified binary
**-R**
: Reassembles a specified assembly file
**-O**
: Obfuscates a specified assembly file

**-p payload**, **--payload payload**
: **Optional** Paths to .s files to be used for obfuscation mode payloads. This flag can be used multiple times to specify multiple payloads to add. These files be named for the function to be called inside them. i.e. [func_name].s

**-m {lazy,no_call}**, **--mode {lazy,no_call}**
: **Optional** The obfuscation mode. Ignored if -O is not present. (default: lazy)

# EXAMPLES
**turbot -D ./binary.o ./disassembled.s**
: The Disassembly module takes a given x86 ELF binary, and uses the Ddisasm library to disassemble down to GAS (Gnu Assembler Syntax), part of the GNU toolchain. You can read more here: https://en.wikipedia.org/wiki/GNU_Assembler.

**turbot -O -p ./payload.s -m lazy ./assembly.s ./modified-assembly.s**
: The insertion stage currently supports two modes, lazy and no call. Lazy insertion will push code right to the top of the executable, and as such the payload will be executed as soon as the program is started. No call insertion will insert the payload after a function call, which renders it functionally useless as it will never be executed, but this can be helpful in modifying the SHA256 hash of the output.

**turbot -R ./assembly.s ./output-binary.o**
: Reassembly calls GCC and recompiles the modified binary back to a usable executable.

**turbot -A -p ./payload.s -m lazy ./binary.o ./filename-prefix**
: -A or -RDO executes all of the functions on a given binary. It will disassemble, obfuscate and reassemble the specified binary. 

# Authors
Written by MasterGomi, pondodev, Franz Tamani, Daalekz, James Hassall, NaveenShank

# BUGS
Submit bug reports online at: <https://github.com/FranzTamani/turBOT/issues>

# SEE ALSO
Full documentation and sources at: <https://github.com/FranzTamani/turBOT/wiki>