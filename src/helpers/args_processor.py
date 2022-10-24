import argparse
from helpers.dates_helper import string_to_date


def valid_date(s):
    try:
        string_to_date(s, format_date='%Y-%m-%d')
        return s
    except ValueError:
        msg = "not a valid date: {0!r}".format(s)
        raise argparse.ArgumentTypeError(msg)


def args_processor():
    parser = argparse.ArgumentParser(
        description='Team reports to json converter',
        epilog='''
        Example:

        1) main.py -o 1 -m general -sd 2022-09-10 -ed 2022-09-20
        2) main.py  --option 1
                    --meeting general
                    --startd 2022-09-10
                    --endd 2022-09-20
        '''
        )
    parser.add_argument('-o', '--option',
                        type=str,
                        choices=["1", "2"],
                        help='Option to process request [1,2]')
    parser.add_argument('-m', '--meeting_name',
                        type=str,
                        help='Name of meeting to search for')
    parser.add_argument('-sd', '--start_date',
                        type=valid_date,
                        help='Start date of meeting (YYYY-MM-DD format)')
    parser.add_argument('-ed', '--end_date',
                        type=valid_date,
                        help='End date of meeting (YYYY-MM-DD format)')

    return vars(parser.parse_args())
