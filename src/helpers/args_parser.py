import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Enter query type, meeting title and date range to get a json formated report.')

    parser.add_argument('query', metavar='Q', type=str, choices=['participants', 'duration'],
                        help='Enter query type')
    parser.add_argument('meeting', metavar='M', type=str, nargs='+',
                        help='Enter meeting title')
    parser.add_argument('dateInit', metavar='dateInit', type=str,
                        help='Enter start date')
    parser.add_argument('dateEnd', metavar='dateEnd', type=str,
                        help='Enter end date')

    return parser.parse_args()