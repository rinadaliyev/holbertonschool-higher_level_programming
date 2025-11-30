#!/usr/bin/python3
"""My documment"""


import json


def serialize_and_save_to_file(data, filename):
    data = json.dumps(data)
    with open(filename, 'w') as f:
        f.write(data)

def load_and_deserialize(filename):
    with open(filename, 'r') as f:
        data = json.loads(f.read())
        return data
