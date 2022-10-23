"""
    Filters in-memory meetings data and uses meeting_name, star_date, end_date, etc...
"""

from utils import convert_timedelta_to_string, date_format_in_full_datetime
from helpers.csv_processor import read_csv_file



def filter_data(meeting_name, date_init, date_end):
    filtered_data = []
    for meeting in organize_data():
        meeting['duration'] = convert_timedelta_to_string(meeting['meeting_end_time'] - meeting['meeting_start_time'])
        if not meeting in filtered_data and meeting['meeting_title'] == meeting_name.lower():
            if meeting['meeting_start_time'] >= date_init and meeting['meeting_start_time'] <= date_end:                               
                filtered_data.append(meeting)
    return filtered_data


def organize_data():

    processed_data = []

    for file in read_csv_file():

        data_model = {
            'total number of participants': 0,
            'meeting title': '',
            'meeting start time': '',
            'meeting end time': '',
            'meeting id': '',
        }
        new_data_model = {}

        for f in file:
            if f in data_model:
                if f == 'meeting start time' or f == 'meeting end time':
                    required_index = file.index(f) + 1
                    date_time_format = date_format_in_full_datetime(file[required_index])
                    data_model[f] = date_time_format
                else:
                    required_index = file.index(f) + 1
                    data_model[f] = file[required_index]
                for item in data_model.items():
                    key, value = item
                    if key == 'total number of participants':
                        new_data_model[key.replace('total number of participants','participants')] = int(value)
                    else:
                        new_data_model[key.replace(' ','_')] = value
        processed_data.append(new_data_model)

    return processed_data
