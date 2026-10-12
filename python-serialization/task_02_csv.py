#!/usr/bin/env python3

import csv
import json

"""
converting between file formats
"""


def convert_csv_to_json(csv_file):
    """convert csv to json"""
    try:
        with open(csv_file, 'r') as f:
            csv_reader = csv.DictReader(f)
            data = []
            for row in csv_reader:
                data.append(row)

        with open('data.json', 'w') as f:
            json.dump(data, f)
            return True
    except:
        return False