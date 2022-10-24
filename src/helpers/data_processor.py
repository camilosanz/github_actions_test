"""
    Filters in-memory meetings data and uses:
    - meeting_name
    - star_date
    - end_date
    - etc
"""
import logging
import os
import string
from helpers import dates_helper
from helpers import json_processor
from helpers.csv_processor import read_line, replace_csv

ATTENDANCE_REPORT_FOLDER_NAME = 'attendance_reports'


def is_valid_path(path):
    if os.path.exists(path):
        return True

    return False


def returns_json_attendance_reports(
    meeting_name: string,
    start_date: string,
    end_date: string,
    option: string
):
    """
        Option=1 => Number of participants
        Option=2 => Duration of meeting
    """
    # Validates 'attendance 'folder exists
    if not is_valid_path(ATTENDANCE_REPORT_FOLDER_NAME):
        warning_message = " Error: 'attendace_reports' folder doesn't exists"
        logging.warning(warning_message)
        return

    start_date = dates_helper.string_to_date(start_date)
    end_date = dates_helper.string_to_date(end_date)
    list_search_range = dates_helper.list_date_range(start_date, end_date)
    # Just list that matches
    data = []
    for search in list_search_range:
        path_sub_folder = os.path.join(ATTENDANCE_REPORT_FOLDER_NAME, search)
        string_date = dates_helper.date_format(search)
        if os.path.exists(path_sub_folder):
            # Lists all file .csv inside folder
            for csv_file_name in os.listdir(path_sub_folder):
                # Asks if contains meeting name
                cont_files = 0

                if csv_file_name.lower().__contains__(meeting_name):
                    path_file = os.path.join(path_sub_folder, csv_file_name)
                    # Opens path to read file
                    with open(path_file, 'r', errors='replace') as csv_file:
                        file_lines = csv_file.readlines()
                        # Gets lines of interest
                        num_part = read_line(file_lines, 1)
                        meeting_startt = read_line(file_lines, 3)
                        meeting_end_time = read_line(file_lines, 4)
                        if option == "1":  # Number participants
                            ls_num_part = replace_csv(num_part)
                            key = "participants"
                            key_variable = int(ls_num_part[1])
                        elif option == "2":  # Duration meeting
                            ls_meeting_startt = replace_csv(meeting_startt)
                            ls_meeting_end_time = replace_csv(meeting_end_time)
                            start_time = dates_helper.string_to_date(
                                ls_meeting_startt[1],
                                format_date='%m/%d/%Y, %H:%M:%S %p'
                                )
                            end_time = dates_helper.string_to_date(
                                ls_meeting_end_time[1],
                                format_date='%m/%d/%Y, %H:%M:%S %p'
                                )
                            key = "duration"
                            key_variable = dates_helper.diff_hour_minute(
                                end_time,
                                start_time
                                )
                    cont_files = len(os.listdir(path_sub_folder))
                    break
                else:
                    if option == "1":
                        key = "participants"
                        key_variable = -99999
                    elif option == "2":
                        key = "duration"
                        key_variable = "0h 0m"
                    cont_files += 1
            if cont_files == len(os.listdir(path_sub_folder)):
                dictionary_format = json_processor.generate_dict(
                    string_date,
                    key,
                    key_variable)
                data.append(dictionary_format)
        else:
            if option == "1":
                key = "participants"
                key_variable = -99999
            elif option == "2":
                key = "duration"
                key_variable = "0h 0m"
            dictionary_format = json_processor.generate_dict(
                string_date,
                key,
                key_variable
                )
            data.append(dictionary_format)
    return json_processor.generate_json(meeting_name.title(), data)
