#!/bin/bash
PORT=${1:-8004}

# start service
python manage.py runserver 0.0.0.0 $PORT