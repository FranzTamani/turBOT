#!/bin/bash

apt update -y
apt install git python3 -y

git clone https://github.com/FranzTamani/turBOT.git

cd turBOT/CLI && \
chmod +x ./setup.sh && \
./setup.sh && \
cp turBOT /usr/bin

mkdir /home/ubuntu/Test
mkdir /home/ubuntu/TestOutput
touch /home/ubuntu/Test/default.o
touch /home/ubuntu/Test/disassemble.o
touch /home/ubuntu/Test/reassemble.asm
touch /home/ubuntu/Test/obfuscate.asm

