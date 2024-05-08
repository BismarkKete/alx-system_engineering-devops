#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
Author: Bismark-K
"""

import requests


def recurse(subreddit, hot_list=[], v_aftr=""):
    "Return None when the subreddit is not valid."
    rqt = requests.get(
            "https://www.reddit.com/r/{}/hot.json".format(subreddit),
            headers={"User-Agent": "Custom"},
            params={"after": v_aftr}
            )

    # Check
    if rqt.status_code == 200:
        for get_data in rqt.json().get("data").get("children"):
            raw_info = get_data.get("data")
            heading = raw_info.get("title")
            hot_list.append(heading)
        v_aftr = rqt.json().get("data").get("after")

        if v_aftr is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, v_aftr)
    else:
        return None
