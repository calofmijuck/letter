FROM python:latest

RUN apt update && apt install cron -y && mkdir logs

ADD requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt && mkdir /letters

COPY mysite /letter-server

COPY run.sh /run.sh

ENTRYPOINT cron && bash /run.sh
