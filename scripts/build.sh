#!/bin/bash

set -e

source ./private/private-env

docker pull redis
docker-compose build --build-arg ngrok_auth_token=$NGROK_AUTH_TOKEN
