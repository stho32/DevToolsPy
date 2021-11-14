#!/bin/python3
import os
import json
import requests
import argparse


def simplify_message(message):
    return message


def get_github_repos(username, page):
    response = requests.get("https://api.github.com/users/" + username + "/repos?page=" + str(page))
    parsed = json.loads(response.content.decode('utf-8'))
    return parsed


def git_clone(username, startswith):
    already_available = []

    for f in os.listdir("."):
        if not os.path.isfile(f):
            already_available.append(f)

    page = 1
    repositories = [""]

    while len(repositories) > 0:
        repositories = get_github_repos(username, page)
        for repository in repositories:
            if (len(startswith) > 0) and (startswith in repository["name"]):
                if repository["name"] in already_available:
                    print("  - " + repository["name"] + " is already here...")
                else:
                    print("  - " + repository["name"] + " cloning...")
                    os.system("git clone " + repository["clone_url"])
        page += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Clone from github repository')
    parser.add_argument('account', type=str, help='which github account is the root of the request')
    parser.add_argument('startswith', type=str, help='a string that the repositories that are cloned start with')
    args = parser.parse_args()

    if len(args.account):
        git_clone(args.account, args.startswith)
