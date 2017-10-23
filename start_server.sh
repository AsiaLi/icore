#!/bin/bash

gunicorn wsgi:application -c config/env.py --reload