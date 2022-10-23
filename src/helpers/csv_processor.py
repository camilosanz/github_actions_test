"""
1. Read CSV files and returns in-memory object
"""

import os
import re


path = os.path.realpath(os.path.join(os.path.dirname(__file__),'..','..','attendance_reports'))


def read_csv_file():
    files_read = []
    for item in get_filename_and_path():
        file_path = os.path.join(item[1], item[0]) 
        with open(file_path, "r", encoding="utf-16") as file:
            data = re.split(r"\n|\t", file.read().lower())
            files_read.append(data)
    return files_read


def get_filename_and_path():
    file_path_name = []
    [ file_path_name.append([file, dirname]) for dirname, dirpath, files in os.walk(path) for file in files ]
    return file_path_name
       


            


