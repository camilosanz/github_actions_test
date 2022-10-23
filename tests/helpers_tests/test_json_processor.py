from src.helpers.json_processor import generate_answer_json
import datetime
import json


def test_generate_answer_json():
    answer_option = 'participants'
    meeting_name = 'Python training'
    date_init = date_end = datetime.datetime(2022, 9, 15, 10, 16, 29)
    date_end = datetime.datetime(2022, 9, 17, 10, 16, 29)
    result = generate_answer_json(
        answer_option, meeting_name,
        date_init, date_end)
    control_params = {
        "meeting_title": "Python training",
        "data": [
            {
                "date": "09/15/2022",
                "participants": -99999
            },
            {
                "date": "09/16/2022",
                "participants": 9
            }
        ]
    }
    control_params_json = json.dumps(control_params, indent=4, sort_keys=False)

    assert result == control_params_json
