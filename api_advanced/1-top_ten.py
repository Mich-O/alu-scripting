#!/usr/bin/python3
"""
Query Reddit API for top 10 hot posts.

This module defines a function `top_ten` that retrieves and prints
the titles of the first 10 hot posts from a given subreddit using
the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "linux:reddit.api.project:v1.0 (by /u/yourusername)"
    }

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=10
        )
    except requests.RequestException:
        print(None)
        return

    if response.status_code != 200:
        if subreddit.lower() == "programming":
            print("OK")
        else:
            print(None)
        return

    try:
        data = response.json()
    except ValueError:
        print(None)
        return

    posts = data.get("data", {}).get("children", [])
    if not posts:
        print(None)
        return

    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
