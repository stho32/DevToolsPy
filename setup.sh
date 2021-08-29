#!/usr/bin/bash

## clone the repo
git clone https://github.com/stho32/DevToolsPy

cd DevToolsPy

## copy the export line to bashrc for global use!
echo "export PATH=\"\$PATH:$(pwd)/source\"" >> ~/.bashrc

