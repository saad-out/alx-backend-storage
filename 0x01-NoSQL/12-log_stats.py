#!/usr/bin/env python3
"""
This module contains the function log_stats that provides some stats
about Nginx logs stored in MongoDB
"""


if __name__ == '__main__':
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    from pymongo import MongoClient

    nginx = MongoClient().logs.nginx
    print("{} logs".format(nginx.count_documents({})))
    print("Methods:")
    print(" method GET: {}".format(nginx.count_documents(
                                                {"method": "GET"}
                                                            )))
    print(" method POST: {}".format(nginx.count_documents(
                                                    {"method": "POST"}
                                                            )))
    print(" method PUT: {}".format(nginx.count_documents(
                                                    {"method": "PUT"}
                                                            )))
    print(" method PATCH: {}".format(nginx.count_documents(
                                                    {"method": "PATCH"}
                                                            )))
    print(" method DELETE: {}".format(nginx.count_documents(
                                                    {"method": "DELETE"}
                                                            )))
    print("{} status check".format(nginx.count_documents(
                                                {"method": "GET",
                                                 "path": "/status"}
                                                        )))
