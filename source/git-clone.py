#!/bin/python3
import os
import subprocess
from prettytable import PrettyTable
import json
import requests

def simplify_message(message):
    return message


def get_github_repos(username, page):
    response = requests.get("https://api.github.com/users/" + username + "/repos?page=" + str(page))
    parsed = json.loads(response.content.decode('utf-8'))
    return parsed

def git_clone(username):
    already_available = []

    for f in os.listdir("."):
        if not os.path.isfile(f):
            already_available.append(f)
    
    page = 1
    repositories = [""]
    
    while (len(repositories) > 0) :
        repositories = get_github_repos(username, page)
        for repository in repositories:
            if repository["name"] in already_available:
                print ("  - " + repository["name"] + " is already here...")
            else:
                print ("  - " + repository["name"] + " cloning...")
                os.system("git clone " + repository["clone_url"])
        page += 1

if __name__ == "__main__":
    git_clone("stho32")

