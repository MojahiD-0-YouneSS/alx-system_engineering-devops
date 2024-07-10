#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    print('OK')
    if not subreddit or not isinstance(subreddit, str):
        return 0
    headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'
    }

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        response.raise_for_status()
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except requests.exceptions.RequestException:
        return 0
