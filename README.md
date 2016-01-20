# tiny-django

A Heroku-ready Django-based Flask replacement.

## Quick Start

    $ mkvirtualenv --python=$(which python3) tiny-django
    $ pip install -r requirements.txt
    $ echo "DEBUG=True" >> .env
    $ echo "PORT=5000" >> .env
    $ foreman start

## Heroku Setup

    $ heroku apps:create
    $ heroku config:set ALLOWED_HOSTS=tiny-django.herokuapp.com
    $ heroku config:set DISABLE_COLLECTSTATIC=1
    $ heroku config:set SECRET_KEY={{ secret_key }}

## Attribution

Based on [Lightweight Django](http://shop.oreilly.com/product/0636920032502.do) by [Julia Elman](https://github.com/juliaelman) and [Mark Lavin](https://github.com/mlavin). See the [original code example](https://github.com/lightweightdjango/examples/tree/chapter-1).
