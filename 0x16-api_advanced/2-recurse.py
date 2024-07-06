#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Reddit API Client; +http://www.example.com)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
    except requests.RequestException:
        return None

    try:
        results = response.json().get("data", {})
    except ValueError:
        return None

    after = results.get("after")
    count += results.get("dist", 0)
    for child in results.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
