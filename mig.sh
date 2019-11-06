#! /bin/bash

python manage.py makemigrations chat
python manage.py migrate
python manage.py runserver 0:8000
