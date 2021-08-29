#!/usr/bin/bash

## clone the repo
git clone https://github.com/stho32/DevToolsPy

## get the current directory
sourcedir = $(pwd)

## copy the export line to bashrc for global use!
echo "export PATH="\$PATH:$sourcedir/DevToolsPy/source"\" >> .bashrc

