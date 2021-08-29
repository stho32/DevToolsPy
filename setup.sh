#!/usr/bin/bash

## we need pip for certain operations
sudo apt install python3-pip

## clone the repo
git clone https://github.com/stho32/DevToolsPy

cd DevToolsPy

## we need that lib for table format
pip3 install -r requirements.txt

## copy the export line to bashrc for global use!
echo "export PATH=\"\$PATH:$(pwd)/source\"" >> ~/.bashrc

cd ..
