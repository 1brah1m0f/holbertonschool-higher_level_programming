#!/usr/bin/python3
"""Docstring for python-input_output.5-save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Docstring for save_to_json_file"""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
