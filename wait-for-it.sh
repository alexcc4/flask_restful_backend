#!/bin/bash
# wait-for-postgres.sh

set -e

#host="$1"
#shift
cmd="$@"

export POSTGRES_USER=app_development
export POSTGRES_PASSWORD=app_development
#until psql -h "$host" -U "$POSTGRES_USER" -c '\l'; do
#  >&2 echo "Postgres is unavailable - sleeping"
#  sleep 1
#done
#
#>&2 echo "Postgres is up - executing command"
#exec $cmd

function postgres_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname="$POSTGRES_USER", user="$POSTGRES_USER", password="$POSTGRES_PASSWORD", host="postgres")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}
#
until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."
exec $cmd