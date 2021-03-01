#!/bin/bash

docker run \
  --rm \
  -itd \
  -v "$(pwd)":/app \
  --name debug-app \
  didrocketlaunchyet_app \
  bash
docker network connect --alias app didrocketlaunchyet_default debug-app
