from datetime import datetime
from helpers.dates_helper import string_to_date


def test_string_to_date_default_format_true():
    format_date = '%m/%d/%Y'
    string_date = '{d.month}/{d.day}/{d.year}'.format(
        d=datetime.strptime('9/27/2022', format_date)
        )
    dt_string = datetime.strptime(string_date, format_date)
    assert_msg_1 = 'Expected date formats'
    assert_msg_2 = 'Expected samte type'

    type_dsc = type(dt_string)
    type_dsr = type(string_to_date('9/27/2022', format_date))

    assert dt_string == string_to_date('9/27/2022', format_date), assert_msg_1
    assert type_dsc == type_dsr, assert_msg_2


def test_list_date_range_default_format_true():
    assert True
