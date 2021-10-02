#!/bin/bash

apt update -y
apt install git python3 -y

git clone https://github.com/FranzTamani/turBOT.git

cd turBOT/CLI && \
chmod +x ./install.sh && \
./install.sh && \
cp turbot /usr/bin

chown -R ubuntu:ubuntu /home/ubuntu

