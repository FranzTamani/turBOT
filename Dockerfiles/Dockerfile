FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y \
    git \
    wget \
    software-properties-common \
    sudo


RUN wget -O - https://download.grammatech.com/gtirb/files/apt-repo/conf/apt.gpg.key | apt-key add -
RUN echo "deb https://download.grammatech.com/gtirb/files/apt-repo focal stable"| sudo tee -a /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y \
    ddisasm \
    python3 \
    rustc \
    clang

RUN git clone https://github.com/FranzTamani/turBOT.git

WORKDIR /turBOT/CLI

RUN chmod +x ./install.sh
RUN ./install.sh

CMD [ "/bin/bash" ]
