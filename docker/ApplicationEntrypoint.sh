#!/bin/sh

pip install -r /app/requirements.txt
#https://flask.palletsprojects.com/en/1.1.x/deploying/uwsgi/
uwsgi --ini uwsgi.ini