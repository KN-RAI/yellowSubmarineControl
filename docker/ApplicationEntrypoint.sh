#!/bin/sh


pip3 install --upgrade pip setuptools wheel
pip3 install -r /app/requirements.txt
#https://flask.palletsprojects.com/en/1.1.x/deploying/uwsgi/
uwsgi --ini uwsgi.ini