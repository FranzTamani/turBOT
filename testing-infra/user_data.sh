#!/bin/bash

wget -O - https://download.grammatech.com/gtirb/files/apt-repo/conf/apt.gpg.key | apt-key add -
echo "deb https://download.grammatech.com/gtirb/files/apt-repo focal stable"| tee -a /etc/apt/sources.list
apt update -y
apt install ddisasm git g++ python3 -y

git clone https://github.com/FranzTamani/TestCLI.git

cd TestCLI && \
chmod +x ./setup.sh && \
./setup.sh
cp turbot /usr/bin

mkdir /home/ubuntu/Test
mkdir /home/ubuntu/TestOutput
touch /home/ubuntu/Test/default.o
touch /home/ubuntu/Test/disassemble.o
touch /home/ubuntu/Test/reassemble.asm
touch /home/ubuntu/Test/obfuscate.asm

