
from utils import date_format_out, date_format_in


def user_question_selection(query, meeting, dateInit, dateEnd):
    user_input = {
        # 'question':'',
        'question_type': '',
        'meeting_title': '**{meeting_name}**',
        'start_date': '**{start_date}**',
        'end_date': '**{end_date}**'
    }
        
    user_input['question_type'] = query
    user_input['meeting_title'] = meeting
    user_input['start_date'] = date_format_in(dateInit)
    user_input['end_date'] = date_format_in(dateEnd)
    # user_input['question'] = questions[user_input['question_type']]

    return user_input

def answer_processor(answer, params):
    questions = {
        'participants':(f'- What is the number of participants attending {params["meeting_title"]} meeting per date, between {date_format_out(params["start_date"])} and {date_format_out(params["end_date"])}'),
        'duration':(f'- What is duration of {params["meeting_title"]} Meeting per date, date filter between {date_format_out(params["start_date"])} and {date_format_out(params["end_date"])}')
    }
    print(f"\n{questions[params['question_type']]}\n\n```json\n{answer}")
