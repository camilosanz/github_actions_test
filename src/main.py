# App entry point
from helpers.args_processor import args_processor
from helpers.data_processor import returns_json_attendance_reports
from helpers.dates_helper import (
    enter_new_dates,
    string_to_date,
    validation_date)
from helpers.json_processor import print_json, writes_json_file


def is_valid_option(selected_option):
    """
        Function that validates if question is ok
        returns True => valid question
                False => invalid question

        valid options => '1','2' or 'q'
    """
    if selected_option == '1':
        return True
    if selected_option == '2':
        return True
    if selected_option == 'q':
        return True
    return False


def process_questions():
    # display questions menu
    # drive "question" selection while not Quit
    """
        returns number
    """
    selected_option = None
    print('Please select an option')
    print('-----------------------')
    # TODO make markdown questions
    template_question = "1. What is the number of Partipants attending \
        'meeting_name' Meeting per date, date filter between 'start_date' \
        and 'end_date'\n"
    template_question += "2. What is the duration of 'meeting_name' \
        Meeting per date, date filter between 'start_date' and 'end_date'\n\n"
    template_question += "Q. Quit\n"

    print(template_question)

    selected_option = input('Option: ').lower()
    valid_option = is_valid_option(selected_option)

    while not valid_option:
        print('Invalid option! Pick again')
        selected_option = input('Option: ').lower()
        valid_option = is_valid_option(selected_option)

    return selected_option


def process_question_options():
    # display input to request meeting name, end and start date
    # drive "input" aquisition while not Quit
    meeting_name = input('Enter meeting name: ')

    start_date_input, end_date_input = enter_new_dates()
    start_date = string_to_date(start_date_input, format_date='%Y-%m-%d')
    end_date = string_to_date(end_date_input, format_date='%Y-%m-%d')

    # TODO Validates dates before reading attendance report
    while not validation_date(start_date, end_date):
        print("\nStart date can't be superior to end date\n")
        start_date, end_date = enter_new_dates()

    arguments = {
        'meeting_name': meeting_name,
        'start_date': start_date_input,
        'end_date': end_date_input
    }
    return arguments


def welcome():
    print('########################################')
    print('##         TEAM ATTENDANCE APP        ##')
    print('########################################\n')


def main():
    welcome()

    args = args_processor()

    if all(args.values()):
        option = args.get('option')
        arguments = args
    else:
        option = process_questions()
        arguments = process_question_options()
    print('Option selected: ', option)

    if option == 'q':
        print("Bye bye!")
        return

    json_data = returns_json_attendance_reports(
        arguments.get('meeting_name'),
        arguments.get('start_date'),
        arguments.get('end_date'),
        option
    )
    print_json(json_data)
    writes_json_file(json_data)


main()
