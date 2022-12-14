FROM python:3.10
LABEL version="1.2.0" \
      description="Team attendance app - Python"

ENV PYTHONUNBUFFERED=1
WORKDIR /attendance_app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./tests /attendance_app/tests
COPY ./src /attendance_app/src
COPY ./attendance_reports/ /attendance_app/attendance_reports
COPY ./README.md .

ENTRYPOINT [ "python3" , "./src/main.py" ]