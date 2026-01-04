#!/usr/bin/python3
"""hm"""

import json

def serialize_and_save_to_file(data, filename):
    """mimim"""
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """mimimi"""
    with open(filename, 'r') as file:
        return json.load(file)
