#!/bin/python3
import datetime
import os
import json
import dateutil.parser
import requests
import argparse
import pytz
import random


def get_github_repos(username, page):
    response = requests.get("https://api.github.com/users/" + username + "/repos?page=" + str(page))
    parsed = json.loads(response.content.decode('utf-8'))
    return parsed


def git_list(username):
    result = []

    repositories_on_page = get_github_repos(username, 1)
    result += repositories_on_page

    page = 2

    there_have_been_repositories_on_that_page = len(repositories_on_page) > 0
    while there_have_been_repositories_on_that_page:
        
        repositories_on_page = get_github_repos(username, page)
        result += repositories_on_page

        there_have_been_repositories_on_that_page = len(repositories_on_page) > 0
        page+=1

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lists repositories with the date of the last push')
    parser.add_argument('account', type=str, help='which github account is the root of the request')
    args = parser.parse_args()

    if len(args.account):
        repositories = git_list(args.account)

        for i in range(1,4):
            repository = random.choice(repositories)
            print(repository["name"])
