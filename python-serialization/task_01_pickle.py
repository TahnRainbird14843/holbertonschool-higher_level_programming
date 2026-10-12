#!/usr/bin/env python3

import pickle

"""
serialization with pickle
"""

class CustomObject:
    """custom object to serialize"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}",
              f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as f:
            try:
                return pickle.load(filename)
            except:
                return None
        return None
    