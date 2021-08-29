#!/bin/python3
import os
import subprocess
from prettytable import PrettyTable

t = PrettyTable(['Repo', 'Status'])

for f in os.listdir("."):
    if not os.path.isfile(f):
        os.chdir(f)
        proc = subprocess.Popen(
            ["git", "pull"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        if "Updating" in out.decode("utf-8"):
            out = "Updated"
        else:
            out = "Already up to date!"
        t.add_row([f, out])
        os.chdir("..")

print(t)
