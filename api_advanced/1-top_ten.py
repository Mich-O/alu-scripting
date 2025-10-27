#!/usr/bin/python3
"""
Module to query Reddit API for hot posts.

This module contains a function to retrieve and display the titles
of the top 10 hot posts from a specified subreddit using the Reddit API.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit: The name of the subreddit to query.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", [])
    if not posts:
        print(None)
        return

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
