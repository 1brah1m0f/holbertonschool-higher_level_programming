#!/usr/bin/python3
"""hm"""

import csv
import json

def convert_csv_to_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as jf:
            json.dump(data, jf)

        return True

    except:
        return False
