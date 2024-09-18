#!/usr/bin/env python3
""" simple helper function """


def index_range(page, page_size):
    """ returns tuple containing a start index and an end index """
    ran = ((page - 1) * page_size, page * page_size)
    return ran
