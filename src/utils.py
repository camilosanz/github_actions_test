from datetime import datetime, timedelta
from pathlib import Path
import os
import re

def date_format_out(date):
    date_formated = datetime.strftime(date, '%m/%d/%Y')
    return date_formated

def date_format_in(date):
    date_formated = datetime.strptime(date, '%m/%d/%Y')
    return date_formated

def date_format_in_full_datetime(date):
    date_formated = datetime.strptime(date, '%m/%d/%Y, %I:%M:%S %p')
    return date_formated

def convert_timedelta_to_string(td):
    hours = td.seconds // 3600
    minutes = (td.seconds - (hours * 3600)) // 60
    return '{}h {}m'.format(hours, minutes)

def generate_dates(date_init, date_end):

    date_range = date_end - date_init
    periods = int(date_range/timedelta(days=1))
    daterange = []

    for day in range(periods):
        date = date_format_out(date_init + timedelta(days = day))
        daterange.append(date)

    return daterange

def get_file_name(meeting_name, start_date, end_date):

    extension = 'json'
    start = start_date.strftime("%m%d")
    end = end_date.strftime("%m%d")
    prefix = meeting_name.replace(' ','_').replace(':','')
    folder_name = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name =  "{}_{}_{}_{}.{}".format(prefix, folder_name, start, end, extension)

    return file_name

def path_existence(path):
    obj=Path(path)
    if not obj.exists():
        os.mkdir(obj)
        print(f'{path} created!')
    else:
        print(f'{path} exists already!')

def input_date_validation(date):
    if re.search("^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$", date):
        return True
    return False


