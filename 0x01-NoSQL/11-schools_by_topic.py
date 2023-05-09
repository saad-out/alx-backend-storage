#!/usr/bin/env python3
"""
This module contains the function schools_by_topic that
returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic: topic searched

    Returns:
        list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
