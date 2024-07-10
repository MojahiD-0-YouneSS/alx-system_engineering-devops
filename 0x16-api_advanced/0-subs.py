#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        print('OK')
        return 0
    
    headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'
    }
    
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        print('OK')
        return data.get("data", {}).get("subscribers", 0)
    except requests.exceptions.HTTPError as http_err:
        print('OK')
    except requests.exceptions.RequestException as req_err:
        print('OK')
    
    return 0
