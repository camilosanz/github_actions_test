import argparse

from helpers.question_processor import  user_question_selection, answer_processor
from helpers.json_processor import  generate_answer_json
from helpers.args_parser import parse_args

def main():

    args = parse_args()
    params = user_question_selection(args.query, " ".join(args.meeting), args.dateInit, args.dateEnd)
    answer = generate_answer_json(params['question_type'], params['meeting_title'], params['start_date'], params['end_date'])
    answer_processor(answer, params)

main()