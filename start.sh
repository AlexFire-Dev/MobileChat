#!/usr/bin/env bash

python3 manage.py collectstatic --clear --noinput
python3 manage.py migrate

daphne -b 0.0.0.0 -p 8000 OnlineChat.asgi:application