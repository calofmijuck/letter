FROM python:latest

RUN apt update && apt install cron -y && mkdir /news-crawler /logs

RUN mkdir /news /news/details /news/overview

ADD requirements.txt /news-crawler/requirements.txt
RUN pip3 install -r /news-crawler/requirements.txt

ADD . /news-crawler/

RUN cp /news-crawler/crontab /etc/cron.d/cron
RUN crontab /etc/cron.d/cron

ENTRYPOINT ["cron", "-f"]
