#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return 0
        print(f"HTTP error occurred: {http_err}")
        return 0
    except requests.exceptions.RequestException as err:
        print(f"Request failed: {err}")
        return 0

    try:
        data = response.json()
    except ValueError:
        print("Failed to parse JSON response")
        return 0

