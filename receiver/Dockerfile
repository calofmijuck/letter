FROM python:latest

RUN pip3 install django python-dotenv && mkdir letters

EXPOSE 80/tcp

COPY mysite /letter-server

RUN ["python3", "/letter-server/manage.py", "makemigrations"]
RUN ["python3", "/letter-server/manage.py", "migrate", "--run-syncdb"]

ENTRYPOINT ["python3", "/letter-server/manage.py", "runserver", "0.0.0.0:80"]
