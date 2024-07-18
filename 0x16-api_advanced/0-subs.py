#!/usr/bin/python3

"""
This module provides a function to query the Reddit API and
retrieve the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If the subreddit is invalid, returns 0.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: The number of subscribers or 0 if the subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Bot/1.0)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response:
        data = response.json()
        Sub =  data['data'].get('subscribers', 0)
        return Sub
    return 0

