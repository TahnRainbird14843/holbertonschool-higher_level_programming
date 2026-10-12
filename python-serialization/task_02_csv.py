#!/usr/bin/env python3

import csv
import json

"""
converting between file formats
"""


def convert_csv_to_json(csv_file):
    """convert csv to json"""
    try: 
        f = open(csv_file, 'r')
        csv_reader = csv.DictReader(f)
        data = []
        for row in csv_reader:
            data.append(row)
    except:
        return False

    try:
        f = open('data.json', 'wb')
        json.dump(data, f)
        return True
    except:
        return False