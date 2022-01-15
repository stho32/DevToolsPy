#!/bin/python3
import os
import subprocess
import shutil
from prettytable import PrettyTable


def simplify_message(message):
    if "unverändert" in message:
        return "CLEAR"
    return "unclean"


def git_status(doIt):
    t = PrettyTable(['Nr.', 'Repo', 'Status', 'Action'])

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
        action = ""
        fulldir = os.path.abspath(os.getcwd())
        os.chdir("..")
        
        if out == "CLEAR":
            if not directory.lower().startswith("devtools") and not directory.lower().startswith("project"):
                action = "Remove"
                if doIt:
                    print(fulldir)
                    shutil.rmtree(fulldir)

        t.add_row([number, directory, out, action])

    t.align = "l"
    if not doIt:
        print(t)


if __name__ == "__main__":
    git_status(False)
    performActionsInput = input("Perform actions (y/N)?")
    if performActionsInput == "y":
        git_status(True)
