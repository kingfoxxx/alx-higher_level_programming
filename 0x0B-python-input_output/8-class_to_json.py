#!/usr/bin/python3

"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """class_to_json return dictionary description with simple data structures
    Args:
        obj : any object for example list, dict
    """
    return obj.__dict__
