from src.helpers.csv_processor import read_csv_file


def test_read_csv_file():
    result = read_csv_file()
    control_params = [
        'meeting title',
        'total number of participants',
        'meeting start time',
        'meeting end time',
        'meeting id'
    ]

    for param in control_params:
        assert param in result[0]
