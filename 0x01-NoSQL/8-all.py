#!/usr/bin/env python3
"""
This module contains the function list_all which returns all documents in a collection
"""
from pymongo.collection import Collection
from typing import List, Dict


def list_all(mongo_collection: Collection) -> List[Dict]:
    """
    Returns all documents in a collection

    Args:
        mongo_collection (Collection): The collection to list from

    Returns:
        list(dict): The list of documents in the collection
    """
    if mongo_collection is None:
        return []

    return [doc for doc in mongo_collection.find()]
