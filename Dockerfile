FROM ubuntu:latest
RUN apt-get update \
    && apt-get install python3 python3-pip -y
WORKDIR /github_actions_test
COPY  requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .