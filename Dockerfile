FROM quay.io/net-sec/python:latest

# install needed packages
RUN apk add --no-cache ffmpeg davfs2
