# test case 14 -- thread safety clang

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
- **language:** c
- **compiler:** clang
- **comments:** links to the `pthread` library
