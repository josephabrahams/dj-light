#!/bin/sh

if [ "$(echo $DEBUG | tr '[:upper:]' '[:lower:]')" = "true" ]; then
    PYTHONUNBUFFERED=True python app.py runserver
else
    waitress-serve --port=$PORT app:application
fi
