# BOT testing suite

this testing suite serves a few purposes:

1. ensure the integrity of BOT's operation
2. provide incremental goals for development and testing
3. emulate real world scenarios that may be encountered

the tests are designed to be passed in order from the first, to last as they have been numbered. they will cover things ranging from hello world written in different languages with different compilers/toolchains all the way to more "realistic" applications that will interact with the OS more intimately as well as maintain a more complex architecture.

there are some assumptions that we are operating under, however:

- all binaries will be compiled for x86 platforms, 32 and 64 bit
- binaries should be compiled to the ELF format, and be runnable on a linux desktop environment (tested on Manjaro Linux)

inside each folder will contain a:

- readme explaining the binary and it's features as well as any other important details
- makefile for compiling the binary fresh, if one so desires
- source code
- the binary itself

## requirements
- make
- gcc
- clang
- [rustc](https://www.rust-lang.org/tools/install)
- valgrind
- strip
- upx (provided in `/bin`)

## usage
each test contains a makefile to reproduce compilation, as well as some other useful functions. there are:
we recommend using _**Ubuntu 12.0.1 or later**
- `make` -- compile and run
- `make run` -- simply run output binary
- `make memleaktest` -- run memory leak test with valgrind (on tests that require it)

there may be more commands available on a test-by-test basis, so read each makefile to understand what is available to you.

## CI Testing
The Makefile included in the root of the testing suite will traverse through all the tests. It checks that the SHA is different to ensure that the file is new and not just a copy. It will also try running turbot with the -A flag. To execute the tests, run make:

- `make` -- runs all tests and outputs logs into test-logs.txt

Alternatively, you can run the script directly and add your own post processing to the console output.

- `./test-script.sh`

# How we test
In this current version of turBOT we have a test suite of 26 tests that we run against our solution to test it's efficacy. To use the testing suite due to clang++ and it's Ubuntu version we recommend using _**Ubuntu 12.0.1 or later**_ as we cannot guarantee that all the test will pass on earlier builds.

***

# Current solution Results
Of the 26 tests, 22 were successful, 4 failed.
The failing tests were:
- 21: Compressed - g++
- 22: Compressed - clang++
- 23: Shared library - g++
- 24: Shared library - clang++

# Failures

## 21 + 22: Compressed (packed) executables
Currently as of build 1.5.2 of ddisasm, compresseed binaries are unable to be interrupted by it and therefore cannot be disassembled. This is due to ddisasm unable to replicate the given program. Until a version of ddisasm is available to do this. Turbot will not work with compressed/packed executables.

### 23 + 24: Shared libraries
Shared libraries fail to recompile at the linking stage due to the library not being included in the recompilation phase, resulting in undefined references. Currently if you are in need of recompiling a piece of source code with shared libraries you will have to recompile it after the obfuscation phase.

## 26: pie with clang++
This test indicates that when testing against our solution against this test it highlights that different versions of ubuntu with clang++ install can produce different results. We recommend that if you are testing against this suite use _**Ubuntu 12.0.1 or later**_. As we have had this test fail on Ubuntu 10.0.0 and are currently unsure the coverage of other distributions and versions so your mileage my vary.

# Summary
The takeaways from this current test coverage is that test 21, 22, 23 and 24 can be grouped together as there isn't any different as of testing that a certain compiler matters.
In terms of points of failure, Please be aware that that because of the current build of ddisasm, the solution is currently unable to handle packed executables, this means that until the dependency allows that this solution will not be able to support that feature. 
Shared libraries are the other point of failure, this is due to how shared libraries work, if you program is needing the use of shared libraries please read the section above.
