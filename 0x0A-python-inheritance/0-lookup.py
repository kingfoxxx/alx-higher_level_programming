#!/usr/bin/python3

"""  returns the list of available attributes
and methods of an objects in file
"""


def lookup(obj):
    """returns the list of available attributes"""
    return dir(obj)
