#!/bin/bash

podman rm -f reolink-recorder
podman run -it -d \
  --privileged \
  --name reolink-recorder \
  -env-file .env \
  localhost/reolink-recorder:dev