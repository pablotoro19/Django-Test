#!/bin/sh
# wait-for.sh

set -e

cmd="$@"

until PGPASSWORD=$DBPASS psql -h "$DBHOST" -U "$DBUSER" -d "$DBNAME" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
