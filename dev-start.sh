#!/bin/bash

podman rm -f reolink-recorder
podman run -it -d \
  --network host \
  --privileged \
  --name reolink-recorder \
  --env-file .env \
  localhost/reolink-recorder:dev