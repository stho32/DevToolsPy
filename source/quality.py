#!/bin/python3
import os
import subprocess
from prettytable import PrettyTable

def check_has_readme():
    if not os.path.isfile("README.md"):
        return "README.md missing"
    if os.stat('README.md').st_size < 1024:
        return "README.md too small"
    return None

def get_subdirectories():
    directories = []

    for f in os.listdir("."):
        if not os.path.isfile(f):
            directories.append(f)

    directories = sorted(directories)
    return directories

def perform_qa_on(directory):
    print("   - performing qa on " + directory + "...")
    result = []
    
    os.chdir(directory)
    message = check_has_readme()
    if not message == None:
        result.append(message)
    os.chdir("..")

    return result;

def perform_qa():
    table = PrettyTable(['Nr.', 'Repo', 'Status'])
    
    number = 0
    directories = get_subdirectories() 

    for directory in directories:
        number += 1
        result = perform_qa_on(directory)
        table.add_row([number, directory, " ".join(result)])

    table.align = "l"

    print(table)

if __name__ == "__main__":
    perform_qa()
