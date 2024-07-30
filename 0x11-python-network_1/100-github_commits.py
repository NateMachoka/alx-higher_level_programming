#!/usr/bin/python3
"""
A script that takes two arguments (repository name and owner name)
Lists the 10 most recent commits of the specified repository
Uses the GitHub API
"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)
    commits = response.json()

    try:
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    except (ValueError, KeyError, TypeError):
        print("Invalid response")
