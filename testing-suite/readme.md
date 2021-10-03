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

- `make` -- compile and run
- `make run` -- simply run output binary
- `make memleaktest` -- run memory leak test with valgrind (on tests that require it)

there may be more commands available on a test-by-test basis, so read each makefile to understand what is available to you.

## CI Testing
The Makefile included in the root of the testing suite will traverse through all the tests. It checks that the SHA is different to ensure that the file is new and not just a copy. It will also try running turbot with the -A flag. To execute the tests, run make:

- `make` -- runs all tests and outputs logs into test-logs.txt

Alternatively, you can run the script directly and add your own post processing to the console output.

- `./test-script.sh`
