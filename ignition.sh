#!/bin/bash

echo "$WEBDAV_URL $WEBDAV_USER $WEBDAV_PASSWORD" >> /etc/davfs2/secrets
mount -t davfs $WEBDAV_URL /Recordings/

python /app/record-ffmpeg.py
