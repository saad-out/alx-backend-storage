#!/usr/bin/env python3
"""
This module contains a class Cache that stores an instance of the Redis client
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Wrapper function that counts how many times methods of the Cache class are
    called

    Args:
        method (Callable): method to wrap

    Returns:
        Callable: wrapped method
    """
    @wraps(method)
    def increment_calls(*args, **kwargs):
        """
        Increment calls of method
        """
        redis_r = args[0]._redis
        redis_r.incr(method.__qualname__)
        return method(*args, **kwargs)
    return increment_calls


def call_history(method: Callable) -> Callable:
    """
    """
    @wraps(method)
    def store_in_out(*args, **kwargs):
        """
        """
        redis_r = args[0]._redis

        input_key: str = str(method.__qualname__) + ":inputs"
        redis_r.rpush(input_key, str(args[1:]))

        output_key: str = str(method.__qualname__) + ":outputs"
        method_output: Any = method(*args, **kwargs)
        redis_r.rpush(output_key, str(method_output))
        return method_output
    return store_in_out


class Cache:
    """
    Redis class that stores instance of the Redis client as a private variable
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def get(
            self,
            key: str,
            fn: Optional[Callable[[bytes], Any]] = None
            ) -> Optional[Any]:
        """
        Get data from Redis instance

        Args:
            key (str): key of the Redis instance
            fn (Optional[Callable[[bytes], Any]]): function to convert data

        Returns:
            Optional[Any]: data converted by fn
        """
        value: Optional[bytes] = self._redis.get(key)
        if not value:
            return None

        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Get data from Redis instance as string

        Args:
            key (str): key of the Redis instance

        Returns:
            Optional[str]: data as string
        """
        return self.get(key, str)

    def get_int(self, key: str) -> Optional[int]:
        """
        Get data from Redis instance as int

        Args:
            key (str): key of the Redis instance

        Returns:
            Optional[int]: data as int
        """
        return self.get(key, int)
