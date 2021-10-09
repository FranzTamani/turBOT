# Docker Setup
To install docker follow the instructions on the get-docker page: https://docs.docker.com/get-docker/

# Build Locally
To build the diocker image yourself, follow the instructions here: https://docs.docker.com/engine/reference/commandline/build/

# Use Pre Built Container inside Docker Hub Repo
## Pulling Pre Built Container
Pull the latest "turbot" image from the docker repo specified below:
[DockerRepo](https://hub.docker.com/r/102114822/turbot)\

Sample Code:
```
 docker pull 102114822/turbot:0.1.0
```
## Running Pre Built Container
After pulling the container follow the instructions from the instructions here: https://docs.docker.com/engine/reference/run/

Sample Code:
```
 docker run -it 102114822/turbot:0.1.0 /bin/bash 
```