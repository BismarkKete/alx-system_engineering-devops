#!/usr/bin/python3
"""
A python function that queries the Reddit API and returns the total number of
subscribers for a given subreddit.
Author: Bismark-K
"""

import requests


def number_of_subscribers(subreddit):
    "The function will return 0 when an invalid subreddit is given."

    rqt = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if rqt.status_code == 200:
        return rqt.json().get("data").get("subscribers")
    else:
        return 0
