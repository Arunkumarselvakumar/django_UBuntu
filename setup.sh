#!/usr/bin/bash
sudo apt install python3-pip -y
python3 -m pip install poetry
python3 -m poetry install
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic