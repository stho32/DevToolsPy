#!/bin/python3
import os

for f in os.listdir("."):
    if not os.path.isfile(f):
        print("  - entering " + f) 
        os.chdir(f)
        print("  - pulling stuff")
        os.system("git pull")
        print("  - exiting " + f)
        os.chdir("..")

