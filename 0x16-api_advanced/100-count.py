#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces.
Author: Bismark-K
"""
import requests


def count_words(subreddit, word_list, arg_aftr=None, num={}):
    """
    This function does exactly what has been described above
    """
    if not word_list or word_list == [] or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"limit": 100}
    if arg_aftr:
        params["after"] = arg_aftr

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    gotten_info = response.json()
    children = gotten_info["data"]["children"]

    for post in children:
        title = post["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title:
                num[word] = num.get(word, 0) + title.count(word.lower())

    arg_aftr = gotten_info["data"]["after"]
    if arg_aftr:
        count_words(subreddit, word_list, arg_aftr, num)
    else:
        sorted_num = sorted(num.items(),
                               key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_num:
            print(f"{word.lower()}: {count}")
