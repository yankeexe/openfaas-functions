from __future__ import unicode_literals
import os
import glob

import youtube_dl
from werkzeug.exceptions import InternalServerError
from flask import Flask, request, send_file, abort


ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
    "source_address": "0.0.0.0",
    "outtmpl": "%(title)s.%(etx)s",
}


def handle(req):
    """handle a request to the function"""
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            data = ydl.extract_info(req, download=False)
            title = data["title"]
            ydl.download([req])

        filename = find_file()

        if not filename:
            raise InternalServerError(
                "Something went wrong in the server. Please try again later."
            )

        return send_file(filename, mimetype="audio/mpeg", as_attachment=True,)
    except youtube_dl.utils.DownloadError as err:
        abort(406, "URL format incorrect.")
    except Exception as err:
        abort(500)
    finally:
        filename = find_file()
        if filename:
            os.remove(filename)


def find_file():
    """Checks if the file is downloaded."""
    globs = glob.glob("*.mp3")

    if len(globs) > 0:
        return globs[0]
    else:
        return False
