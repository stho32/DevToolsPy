#!/bin/python3
import os
import subprocess
from prettytable import PrettyTable
import json
import requests

def simplify_message(message):
    return message


def get_github_repos(username):
    response = requests.get("https://api.github.com/users/" + username + "/repos?per_page=1000")
    parsed = json.loads(response.content.decode('utf-8'))
    return parsed

def git_clone(username):
    already_available = []

    for f in os.listdir("."):
        if not os.path.isfile(f):
            already_available.append(f)
    
    repositories = get_github_repos(username)
    for repository in repositories:
        if not repository["name"] in already_available:
            os.system("git clone " + repository["clone_url"])

if __name__ == "__main__":
    git_clone("stho32")

