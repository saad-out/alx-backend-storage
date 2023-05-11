#!/usr/bin/env python3
"""
This module contains a function that returns the HTML content of a particular
URL and stores it in a Redis cache
"""
import redis
import requests
from typing import Optional, Callable
from functools import wraps


def count_url_calls(fn: Callable) -> Callable:
    """
    Wrapper function that counts how many times a URL is called

    Args:
        fn (Callable): function to wrap

    Returns:
        Callable: wrapped function
    """
    @wraps(fn)
    def increment_url_count(*args, **kwargs):
        """
        Increment calls of method
        """
        r: redis.Redis = redis.Redis()
        url: str = ''
        if args:
            url = args[0]
        if kwargs:
            url = kwargs["url"] if "url" in kwargs else url
        if not r.get("count:{}".format(url)):
            r.set("count:{}".format(url), 1)
            r.expire("count:{}".format(url), 10)
        else:
            r.incr("count:{}".format(url))
        return fn(*args, **kwargs)
    return increment_url_count


@count_url_calls
def get_page(url: str) -> str:
    """
    Returns the HTML content of the URL

    Args:
        url (str): URL to request

    Returns:
        str: HTML content of the URL
    """
    r: redis.Redis = redis.Redis()

    page_cache: Optional[bytes] = r.get(url)
    html_content: Optional[str] = ''
    if page_cache:
        html_content = str(page_cache)
    else:
        html_content = requests.get(url).text
        r.set(url, html_content)
        r.expire(url, 10)

    return html_content
