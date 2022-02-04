#!/bin/python3
import datetime
import os
import json
import dateutil.parser
import requests
import argparse
import pytz


def simplify_message(message):
    return message


def get_github_repos(username, page):
    response = requests.get("https://api.github.com/users/" + username + "/repos?page=" + str(page))
    parsed = json.loads(response.content.decode('utf-8'))
    return parsed


def git_list(username):
    already_available = []

    for f in os.listdir("."):
        if not os.path.isfile(f):
            already_available.append(f)

    page = 1
    repositories = [""]
    today = datetime.datetime.now()
    too_old_date = (today - datetime.timedelta(days=365*2))
    too_old_date = pytz.UTC.localize(too_old_date)

    while len(repositories) > 0:
        repositories = get_github_repos(username, page)
        for repository in repositories:
            last_push = dateutil.parser.parse(repository["pushed_at"]) #, "%Y-%m-%dT%H:%M:%SZ"
            if last_push < too_old_date:
                print("  - too old: " + repository["name"] + " from " + repository["pushed_at"])
        page += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lists repositories with the date of the last push')
    parser.add_argument('account', type=str, help='which github account is the root of the request')
    args = parser.parse_args()

    if len(args.account):
        git_list(args.account)
