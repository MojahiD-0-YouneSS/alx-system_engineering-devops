#!/usr/bin/python3
"""
Contains the number_of_subscribers function.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0\
                (by /u/firdaus_cartoon_jr)'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0

    data = response.json().get("data", {})
    subscribers = data.get("subscribers", 0)

    return subscribers
