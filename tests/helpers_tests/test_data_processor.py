from src.helpers.data_processor import filter_data, organize_data
import datetime


def test_organize_data():
    result = organize_data()
    control_params = {
        'participants': 10,
        'meeting_title': 'training branches: database basics on tsql',
        'meeting_start_time': datetime.datetime(2022, 4, 25, 8, 22, 11),
        'meeting_end_time': datetime.datetime(2022, 4, 25, 10, 16, 29),
        'meeting_id': 'bf2dbe01-58bd-491d-b4a6-7e9bacabbeb1'
    }

    assert control_params in result


def test_filter_data():
    meeting_name = 'training branches: database basics on tsql'
    date_init = datetime.datetime(2022, 4, 25, 8, 22, 11)
    date_end = datetime.datetime(2022, 4, 25, 10, 16, 29)
    result = filter_data(meeting_name, date_init, date_end)
    control_params = {
        'participants': 10,
        'meeting_title': 'training branches: database basics on tsql',
        'meeting_start_time': datetime.datetime(2022, 4, 25, 8, 22, 11),
        'meeting_end_time': datetime.datetime(2022, 4, 25, 10, 16, 29),
        'meeting_id': 'bf2dbe01-58bd-491d-b4a6-7e9bacabbeb1',
        'duration': '1h 54m'
    }

    assert result[0] == control_params
