#!/usr/bin/env python3
"""
This module contains the function update_topics that changes all topics of a
school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name

    Args:
        mongo_collection: the pymongo collection object
        name: the school name to update
        topics: the list of topics approached in the school

    Returns:
        Nothing
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
