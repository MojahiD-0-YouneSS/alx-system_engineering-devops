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
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Reddit API Client; +http://www.example.com)'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return 0
    except ValueError as e:
        print(f"JSON parsing failed: {e}")
        return 0

    return subscribers
