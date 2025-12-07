#!/bin/bash
set -o errexit

pip install -r requirements.txt
cd fynd_task2
python manage.py migrate
