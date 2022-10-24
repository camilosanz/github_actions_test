"""
1. Genenerates JSON from in-memory object
2. Writes in-memory object into JSON file
"""
import json
import os
from datetime import datetime

OUTPUT_DIR = 'output'


def generate_json(string_meeting_title, list_data):
    json = {
        "meeting_title": string_meeting_title,
        "data": list_data
    }
    return json


def generate_dict(string_date, key, key_variable):
    dictionary = {
        "date": string_date,
        key: key_variable
    }
    return dictionary


def print_json(json_string):
    print(json.dumps(json_string, indent=4))


def create_folder(path):
    # Check folder structure
    if not os.path.exists(path):
        os.mkdir(path)


def get_timestamp_string():
    return datetime.now().strftime("%Y%m%d%H%M%S")


def get_filename(prefix="json", extension="json"):
    """
    Build filename using:
     'prefix' => Strign
     'suffix' => Build from timestamp yyyymmHHMMSS
     'extension' => String
    Output is: 'prefix'_'sufix'.'extension'
    """
    return "{}_{}.{}".format(prefix, get_timestamp_string(), extension)


def writes_json_file(data):
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    json_path_folder = os.path.join(OUTPUT_DIR, get_filename())
    with open(json_path_folder, 'w') as json_file:
        json_object = json.dumps(data, indent=4)
        json_file.write(json_object)
