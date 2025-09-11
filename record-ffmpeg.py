#!/bin/env python

import os
import time
import datetime
import subprocess

# RTSP-URL deiner Reolink-Kamera
RTSP_URL = os.getenv("REOLINK_STREAMING_URl")

# Basisverzeichnis für Aufnahmen
BASE_DIR = os.getenv("TARGET_DIRECTORY")

def get_next_half_hour():
    now = datetime.datetime.now()
    minute = 30 if now.minute < 30 else 60
    next_half_hour = now.replace(minute=0, second=0, microsecond=0) + datetime.timedelta(minutes=minute)
    return next_half_hour

def get_output_path(start_time, end_time):
    date_folder = start_time.strftime("%Y-%m-%d")
    filename = f"{start_time.strftime('%H_%M')}-{end_time.strftime('%H_%M')}.mp4"
    folder_path = os.path.join(BASE_DIR, date_folder)
    os.makedirs(folder_path, exist_ok=True)
    return os.path.join(folder_path, filename)

def record_block():
    now = datetime.datetime.now()
    end_time = get_next_half_hour()
    duration = int((end_time - now).total_seconds())
    output_file = get_output_path(now, end_time)
    print(f"Starte Aufnahme: {output_file} für {duration} Sekunden")
    cmd = [
        "ffmpeg",
        "-rtsp_transport", "tcp",
        "-fflags", "+genpts",
        "-flags", "+low_delay",
        "-analyzeduration", "1000000",
        "-probesize", "1000000",
        "-i", RTSP_URL,
        "-t", str(duration),
        "-c", "copy",
        "-f", "mp4",
        output_file
    ]
    print(" ".join(cmd))
    subprocess.run(cmd, timeout=duration + 60)

if __name__ == "__main__":
    while True:
        record_block()
        time.sleep(1)
