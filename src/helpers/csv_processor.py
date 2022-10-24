"""
1. Read CSV files and returns in-memory object
"""


def read_line(file_lines, line_number):
    return file_lines[line_number]


def replace_csv(csv_string):
    return csv_string.replace('\x00', '').replace('\n', '').split('\t')
