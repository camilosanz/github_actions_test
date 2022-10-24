from helpers.data_processor import (
    is_valid_path,
    returns_json_attendance_reports)


def test_is_valid_path_att_rep_true():
    att_rep_fold_name = 'attendance_reports'
    assert_msj = 'Exists path of folder exists'
    assert is_valid_path(att_rep_fold_name), assert_msj


def test_is_valid_path_att_rep_false():
    another_fold_name = 'another_ridiculouse_folder_name'
    assert_msj = "Path of folder doesn't exists"
    assert not is_valid_path(another_fold_name), assert_msj


def test_returns_json_attendance_reports_general_number_participants_true():
    meeting_name = 'general'
    start_date = '2022-9-10'
    end_date = '2022-9-17'
    option = '1'  # Participants

    expected_result = {
        "meeting_title": "General",
        "data": [
            {
                "date": "9/10/2022",
                "participants": -99999
            },
            {
                "date": "9/11/2022",
                "participants": -99999
            },
            {
                "date": "9/12/2022",
                "participants": -99999
            },
            {
                "date": "9/13/2022",
                "participants": -99999
            },
            {
                "date": "9/14/2022",
                "participants": -99999
            },
            {
                "date": "9/15/2022",
                "participants": -99999
            },
            {
                "date": "9/16/2022",
                "participants": 22
            },
            {
                "date": "9/17/2022",
                "participants": -99999
            }
        ]
    }

    result = returns_json_attendance_reports(
        meeting_name,
        start_date,
        end_date,
        option
    )
    assert_msj = "Json reports are equal"
    assert expected_result == result, assert_msj
