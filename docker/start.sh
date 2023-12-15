#!/bin/bash

python3 manage.py flush --no-input
make migrate
gunicorn -b=0.0.0.0:8000 task_manager.wsgi:application --workers 4
