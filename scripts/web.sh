#!/bin/sh

if [ "$(echo $DEBUG | tr '[:upper:]' '[:lower:]')" = "true" ]; then
    PYTHONUNBUFFERED=True python web.py runserver
else
    waitress-serve --port=$PORT web:application
fi
