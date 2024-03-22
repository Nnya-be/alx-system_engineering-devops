#!/usr/bin/python3
"""Returns the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    header = {'User-Agent': 'myapp'}
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

