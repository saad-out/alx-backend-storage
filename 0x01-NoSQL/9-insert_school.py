#!/usr/bin/env python3
"""
This module contains the function insert_school that inserts a new document
in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs

    Args:
        mongo_collection: the pymongo collection object
        kwargs: key-value pairs to be inserted in the document

    Returns:
        InsertOneResult.id: the new _id for the new document
    """
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
