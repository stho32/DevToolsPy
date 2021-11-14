#!/bin/python3
import os
import subprocess


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
    result = []

    os.chdir(directory)
    message = check_has_readme()
    if message is not None:
        result.append(message)
    os.chdir("..")

    return result


def perform_qa():
    directories = get_subdirectories()

    for directory in directories:
        result = perform_qa_on(directory)
        if len(result) > 0:
            print(directory + ":")
            for message in result:
                print("  - " + message)
            exit()


if __name__ == "__main__":
    perform_qa()
