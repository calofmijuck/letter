FROM python:latest

RUN apt update && apt install cron -y && service cron start && mkdir logs

ADD requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt && mkdir letters

COPY mysite /letter-server

RUN ["python3", "/letter-server/manage.py", "makemigrations"]
RUN ["python3", "/letter-server/manage.py", "migrate", "--run-syncdb"]

ENTRYPOINT ["python3", "/letter-server/manage.py", "runserver", "0.0.0.0:80"]
