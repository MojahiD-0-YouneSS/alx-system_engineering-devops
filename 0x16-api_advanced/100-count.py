#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles, and prints a
sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, hot_list=None, viewed_count=0, after=''):
    """
    Queries the Reddit API, parses the title of all hot articles, and prints a
    sorted count of given keywords.
    """
    if hot_list is None:
        hot_list = []

    base_url = 'https://www.reddit.com/'
    endpoint = 'r/{}/hot.json'.format(subreddit)
    query_string = '?show="all"&limit=100\
            &after={}&count={}'.format(after, viewed_count)
    url = base_url + endpoint + query_string
    headers = {'User-Agent': 'Python/1.0(Holberton School 0x16 task 3)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.RequestException:
        return

    try:
        data = response.json().get('data', {})
    except ValueError:
        return

    for post in data.get('children', []):
        hot_list.append(post.get('data', {}).get('title', '')) 
    after = data.get('after', '')
    dist = data.get('dist', 0)
    if after:
        count_words(subreddit, word_list, hot_list, viewed_count + dist, after)

    if viewed_count == 0:
        result = {}
        word_list = [word.lower() for word in word_list]
        hot_words = ' '.join(hot_list).lower().split()

        for hot_word in hot_words:
            if hot_word in word_list:
                result[hot_word] = result.get(hot_word, 0) + 1

        for word, count in sorted(result.items(), key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(word, count))
