#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Reddit API Client; +http://www.example.com)"
    }
    params = {
        "limit": 10
    }
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
        results = response.json().get("data")
        if results:
            for child in results.get("children", []):
                print(child.get("data", {}).get("title"))
        else:
            print("None")
    except requests.RequestException as e:
        print("None")
    except ValueError:
        print("None")


