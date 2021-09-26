# test case 21 -- compressed g++

## expected functionality
prints out the following lines:
```
consumed resource: 87
consumed resource: 17
consumed resource: 91
consumed resource: 100
consumed resource: 17
```
and exits with code 0.

## technical details
- **language:** c++
- **compiler:** g++
- **comments:** links to the `pthread` library, binary is compressed with upx
