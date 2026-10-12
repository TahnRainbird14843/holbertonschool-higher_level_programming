#!/usr/bin/env python3

import json

"""
serializing and deserialising data in python
"""


def serialize_and_save_to_file(data, filename):
    """serialize data to file"""
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """deserialize data"""
    with open(filename, 'r') as f:
        return json.load(f)
