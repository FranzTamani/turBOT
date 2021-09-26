# test case 24 -- shared library clang++

## expected functionality
prints out hello world and exits with code 0.

## technical details
- **language:** c++
- **compiler:** clang++
- **comments:** shared library source and .so file is in `include/`. can be compiled with the makefile in the same folder. compiled binary should be run using the makefile so the appropriate environment variable is set.
