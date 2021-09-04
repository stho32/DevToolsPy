#!/bin/python3
import os
import subprocess
from prettytable import PrettyTable

def simplify_message(message):
    return message

def git_status():
    t = PrettyTable(['Repo', 'Status'])

    for f in os.listdir("."):
        if not os.path.isfile(f):
            os.chdir(f)
            proc = subprocess.Popen(["git", "push"], stdout=subprocess.PIPE)
            (out, err) = proc.communicate()
            out = simplify_message(out.decode("utf-8"))
            t.add_row([f, out])
            os.chdir("..")

    t.align = "l"
    print(t)

if __name__ == "__main__":
    git_status()
