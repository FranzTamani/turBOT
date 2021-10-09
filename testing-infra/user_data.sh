#!/bin/bash

apt-get install -y wget

wget -O - https://download.grammatech.com/gtirb/files/apt-repo/conf/apt.gpg.key | apt-key add -
echo "deb https://download.grammatech.com/gtirb/files/apt-repo focal stable"| tee -a /etc/apt/sources.list
apt update -y
apt-get install -y \
    ddisasm \
    git \
    python3 \
    rustc \
    clang \

git clone https://github.com/FranzTamani/turBOT.git

cd turBOT/CLI && \
chmod +x ./install.sh && \
./install.sh && \
cp turbot /usr/bin

chown -R ubuntu:ubuntu /home/ubuntu

