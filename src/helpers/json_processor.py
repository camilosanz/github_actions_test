"""
1. Genenerates JSON from in-memory object
2. Writes in-memory object into JSON file
"""

from helpers.data_processor import  filter_data
from utils import date_format_out, generate_dates, get_file_name, path_existence
import json
import os


def write_data_json_file(data, meeting_name, start_date, end_date):

    path = os.path.realpath(os.path.join(os.path.dirname(__file__),'..','..','attendance_reports_queries'))
    file_name = get_file_name(meeting_name, start_date, end_date)
    path_existence(path)
    filename = os.path.join(path, file_name)

    with open(filename, 'w') as openfile:
        openfile.write(data)

    

def generate_answer_json(answer_option, meeting_name, date_init, date_end):
    answer = {
        'meeting_title': meeting_name,
        'data': []
    }    
    answer_data_format = {
        'participants':-99999,
        'duration': "0h 0m"
    }
    meeting_dates_list = []
    meeting_data_per_date = {}

    for meeting in filter_data(meeting_name, date_init, date_end):
        meeting_date = date_format_out(meeting['meeting_start_time'])
        meeting_dates_list.append(meeting_date)
        meeting_data_per_date[meeting_date] = meeting[answer_option]

    for date in generate_dates(date_init, date_end):
        if not date in meeting_dates_list:
            answer_data = {'date':date, answer_option:answer_data_format[answer_option]}
        else:
            answer_data = {'date':date, answer_option: meeting_data_per_date[date]}
        answer['data'].append(answer_data)
    
    json_answer = json.dumps(answer, indent=4, sort_keys=False)
    write_data_json_file(json_answer, meeting_name, date_init, date_end)

    return json_answer
