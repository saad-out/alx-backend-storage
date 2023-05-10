#!/usr/bin/env python3
"""
This module contains a class Cache that stores an instance of the Redis client
"""
import redis
from typing import Union
import uuid


class Cache:
    """
    Redis class that stores instance of the Redis client as a private variable
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis instance

        Args:
            data (Union[str, bytes, int, float]): data to store

        Returns:
            str: key of the Redis instance
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
