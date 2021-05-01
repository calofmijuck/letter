#!/bin/bash

python3 /letter-server/manage.py makemigrations
python3 /letter-server/manage.py migrate --run-syncdb

python3 /letter-server/manage.py crontab add

python3 /letter-server/manage.py runserver 0.0.0.0:80 >> /logs/django.logs 2>&1
