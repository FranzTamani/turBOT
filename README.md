# turBOT
Binary Obfuscation Tool

To learn more about the solution, please see the [wiki](https://github.com/FranzTamani/turBOT/wiki)

## Remote VM via AWS EC2
To learn about deploying an AWS EC2 testing infra with all pre-requisite software installed see the testing-infra [README](https://github.com/FranzTamani/turBOT/tree/main/testing-infra)

## Docker Container Environment
To learn about the dockerised development environment see the Dockerfiles [README](https://github.com/FranzTamani/turBOT/tree/main/Dockerfiles)

## CI Testing
To run all integration tests inside the testing suite. Navigate to ./testing-suite and run the following.

- `make` -- runs all tests and outputs logs into test-logs.txt

Alternatively, you can run the script directly and add your own post processing to the console output.

- `./test-script.sh`
