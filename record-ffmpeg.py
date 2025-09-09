#!/bin/env python

import os
import time
import datetime
import subprocess

# RTSP-URL deiner Reolink-Kamera
RTSP_URL = "rtsp://user-env:pw-env@10.1.2.70:554/h264Preview_01_main"

# Basisverzeichnis für Aufnahmen
BASE_DIR = "/Recordings/ffmpeg"

# Dauer eines Blocks in Sekunden (30 Minuten)
BLOCK_DURATION = 30 * 60

def get_output_path():
    now = datetime.datetime.now()
    date_folder = now.strftime("%Y-%m-%d")
    start_time = now.strftime("%H_%M")
    end_time = (now + datetime.timedelta(seconds=BLOCK_DURATION)).strftime("%H_%M")
    filename = f"{start_time}-{end_time}.mp4"
    folder_path = os.path.join(BASE_DIR, date_folder)
    os.makedirs(folder_path, exist_ok=True)
    return os.path.join(folder_path, filename)

def record_block():
    output_file = get_output_path()
    print(f"Starte Aufnahme: {output_file}")
    cmd = [
        "ffmpeg",
        "-i", RTSP_URL,
        "-t", str(BLOCK_DURATION),
        "-vcodec", "copy",
        "-acodec", "copy",
        output_file
    ]
    print(" ".join(cmd))
    ##subprocess.run(cmd)

if __name__ == "__main__":
    while True:
        record_block()
        time.sleep(1)  # kleine Pause zwischen den Blöcken
