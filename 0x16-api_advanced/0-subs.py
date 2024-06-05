#!/usr/bin/python3
"""
A python function that queries the Reddit API and returns the total number of
subscribers for a given subreddit.
Author: Bismark-K
"""

import requests


def number_of_subscribers(subreddit):
    "The function will return 0 when an invalid subreddit is given."

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom"}

    rspns = requests.get(url, headers=headers, allow_redirects=False)

    if rspns.status_code == 200:
        try:
            data = rspns.json()
            return data.get("data").get("subscribers", 0)
        except ValueError:
            return 0
    else:
        return 0
