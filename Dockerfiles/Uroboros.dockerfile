FROM debian:stretch

RUN apt-get update \
    && apt-get install -y build-essential ca-certificates curl git \
        devscripts debhelper opam \
    && rm -rf /var/lib/apt/lists/*

RUN cd /root \
    && yes | opam init \
    && opam switch 4.01.0
RUN eval `opam config env` \
    && opam install 'deriving=0.7' 'ocamlfind=1.5.5' 'parmap=1.0-rc6' 'batteries=2.3.1' 'ocamlbuild'

RUN apt-get install -y git \
    && cd /root \
    && git clone https://github.com/s3team/uroboros \
    && eval `opam config env` \
    && cd /root/uroboros/src \
    && ./build

WORKDIR /root

CMD [ "/bin/bash" ]