#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the first ten
hot posts listed in a given subreddit
Author: Bismark-K.
"""

import requests


def top_ten(subreddit):
    "function will print None if not a valid subreddit."
    rqt = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )
    # Check
    if rqt.status_code == 200:
        for get_data in rqt.json().get("data").get("children"):
            raw_info = get_data.get("data")
            heading = raw_info.get("title")
            print(heading)
    else:
        print(None)
