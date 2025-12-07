#!/bin/bash
set -o errexit

pip install -r requirements.txt
python fynd_task2/manage.py migrate
python fynd_task2/manage.py collectstatic --noinput
