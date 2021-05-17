FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y git software-properties-common


RUN add-apt-repository ppa:mhier/libboost-latest 
RUN echo "deb [trusted=yes] https://grammatech.github.io/gtirb/pkgs/focal ./" | tee -a /etc/apt/sources.list.d/gtirb.list 
RUN apt-get update \
    && apt-get install ddisasm


WORKDIR /root

CMD [ "/bin/bash" ]
