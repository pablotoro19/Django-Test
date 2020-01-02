#!/bin/sh

# You need to specify the environment variable of the upstream uwsgi at docker run

sed -i "s/<GUNICORN_SERVER_IP>/${GUNICORN_SERVER_IP}/" /etc/nginx/nginx.conf
exec "$@"
