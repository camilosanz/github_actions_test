FROM python:alpine3.16
LABEL version="1.2.0" \
      description="Team attendance app - Python"

# ENVOutput will be directally send to docker log stdout, stderr
# Without beeing buffered
ENV PYTHONUNBUFFERED=1
WORKDIR /attendance_app

COPY ./requirements.txt ./requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# Copying folders and application files
COPY ./tests /attendance_app/tests
COPY ./src /attendance_app/src
COPY ./attendance_reports/ /attendance_app/attendance_reports
COPY ./Readme.md .

ENTRYPOINT [ "python3" , "./src/main.py" ]
