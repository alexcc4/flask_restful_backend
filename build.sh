#!/usr/bin/env bash

set -u

cd $(pwd)

# image name
N=app_api

L=.env.local.latest
T=.env.local.$(date +%Y%m%d%H%M%S)

grep = .env.${PYTHON_ENV} | awk '{print "export " $0}'| tee ${L} > ${T}
source ${T}

V=$(date +%F)

# build image api from Dockerfile
docker build -t "${N}:${V}" -t "${N}:latest" .


docker-compose up -d
# wait for postgresql ready for connection
sleep 15

docker-compose exec -T api python3 manage.py db migrate
docker-compose exec -T api python3 manage.py db upgrade