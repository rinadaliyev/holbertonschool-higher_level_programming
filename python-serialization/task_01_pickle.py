#!/usr/bin/env python3
"""My doadsiufhopasd ipusdhfiashfio"""


import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """Serialize the current object to a file using pickle."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None  # Any write/serialization error returns None

    @classmethod
    def deserialize(cls, filename: str):
        """Deserialize a CustomObject instance from a file using pickle."""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)

            # Verify the loaded object is actually a CustomObject
            if isinstance(obj, cls):
                return obj
            return None

        except Exception:
            return None  # File missing, corrupted, or invalid pickle
