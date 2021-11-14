#!/bin/python3
import os
import subprocess
from prettytable import PrettyTable


def simplify_pull_message(message):
    if "Updating" in message:
        return "Updated!"
    if "Enumerating" in message:
        return "Updated!"
    if "Aktualisiere" in message:
        return "Updated!"
    if "Already" in message:
        return "Up to date!"
    if "Bereits" in message:
        return "Up to date!"
    return message


def pull_all_repos():
    t = PrettyTable(['Repo', 'Status'])

    for f in os.listdir("."):
        if not os.path.isfile(f):
            print("  - pulling updates for " + f)

            os.chdir(f)
            proc = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
            (out, err) = proc.communicate()
            out = simplify_pull_message(out.decode("utf-8"))
            t.add_row([f, out])
            os.chdir("..")

    t.align = "l"
    print(t)


def debug_simple_pull():
    proc = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    print(out)


if __name__ == "__main__":
    pull_all_repos()
