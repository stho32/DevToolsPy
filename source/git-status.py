#!/bin/python3
import os
import subprocess
from prettytable import PrettyTable


def simplify_message(message):
    if "unverändert" in message:
        return "CLEAR"
    return "unclean"


def git_status():
    t = PrettyTable(['Nr.', 'Repo', 'Status'])

    number = 0
    directories = []

    for f in os.listdir("."):
        if not os.path.isfile(f):
            directories.append(f)

    directories = sorted(directories)

    for directory in directories:
        number += 1
        os.chdir(directory)
        proc = subprocess.Popen(["git", "status"], stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = simplify_message(out.decode("utf-8"))
        t.add_row([number, directory, out])
        os.chdir("..")

    t.align = "l"
    print(t)


if __name__ == "__main__":
    git_status()
