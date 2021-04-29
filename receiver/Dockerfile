FROM python:latest

RUN apt update && apt install cron -y && mkdir logs
RUN service cron start

ADD requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt && mkdir -p letters/failed

COPY mysite /letter-server

RUN chmod 0744 /letter-server/crontab && cp /letter-server/crontab /etc/cron.d/cron
RUN crontab /etc/cron.d/cron

RUN ["python3", "/letter-server/manage.py", "makemigrations"]
RUN ["python3", "/letter-server/manage.py", "migrate", "--run-syncdb"]

ENTRYPOINT cron && python3 /letter-server/manage.py runserver 0.0.0.0:80
