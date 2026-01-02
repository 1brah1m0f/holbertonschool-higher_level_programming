#!/usr/bin/python3
"""Docstring for python-input_output.4-from_json_string"""


import json


def load_from_json_file(filename):
    """hm what is that"""
    with open(filename, "r") as f:
        return json.load(f)
