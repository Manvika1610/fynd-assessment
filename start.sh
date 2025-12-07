#!/bin/bash
cd fynd_task2
exec gunicorn fynd_task2.wsgi --log-file -
