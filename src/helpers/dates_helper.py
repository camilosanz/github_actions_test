from datetime import datetime, timedelta


def list_date_range(
    start_date: datetime,
    end_date: datetime,
    format_date="%m%d%Y"
):
    """
        Devuelve una lista en el rango de fechas indicado
            Input start_date = type(datetime)
            Input end_date = type(datetime)
        return Ex. ['09012020', '09022020', '09032020']
    """
    diff_days = end_date - start_date
    days = [(start_date+timedelta(days=i)).date().strftime(format_date)
            for i in range(diff_days.days + 1)]
    return days


def date_format(string_date, format_date='%m%d%Y'):
    return '{d.month}/{d.day}/{d.year}'.format(
        d=datetime.strptime(string_date, format_date)
        )


def string_to_date(string_date, format_date='%Y-%m-%d'):
    return datetime.strptime(string_date, format_date)


def diff_hour_minute(end_date: datetime, start_date: datetime, format_date=''):
    diff = end_date - start_date
    duration_in_s = diff.total_seconds()

    div_mod = divmod(duration_in_s, 3600)

    hours = div_mod[0]
    minutes = divmod(div_mod[1], 60)[0]

    return '{}h {}m'.format(round(hours), round(minutes))


def validation_date(start_date: datetime, end_date: datetime):
    if (start_date > end_date):
        return False
    return True


def enter_date_format(input_date, format_date="%Y-%m-%d"):
    try:
        datetime.datetime.strptime(input_date, format_date)
    except ValueError:
        print("Incorrect format. Format [YYYY-MM-DD]!\n")
        return enter_date_format()


def enter_new_dates():
    # TODO make mask input on date
    start_date_input = input('Enter a start date in YYYY-MM-DD format: ')
    end_date_input = input('Enter a end date in YYYY-MM-DD format: ')
    try:
        string_to_date(start_date_input, format_date='%Y-%m-%d')
        string_to_date(end_date_input, format_date='%Y-%m-%d')
    except ValueError:
        print("\nSorry, some date is in the incorrect format. Try again!")
        return enter_new_dates()
    return start_date_input, end_date_input
