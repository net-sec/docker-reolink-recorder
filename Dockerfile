FROM quay.io/net-sec/python:latest

# install needed packages
RUN apk add --no-cache ffmpeg davfs2

RUN mkdir /app

COPY ./record-ffmpeg.py /app
COPY ./ignition.sh /app

RUN mkdir /Recordings
RUN chmod +x /app/ignition.sh

ENTRYPOINT "/app/ignition.sh"
