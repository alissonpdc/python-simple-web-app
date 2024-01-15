#!/bin/bash

echo "==> Starting makemigrations"
python manage.py makemigrations
python manage.py makemigrations tasks

echo "==> Starting migrate"
python manage.py migrate

echo "==> DB updated"