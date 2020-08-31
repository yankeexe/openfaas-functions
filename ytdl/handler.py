from __future__ import unicode_literals
import os
import glob

import youtube_dl
from flask import Flask, render_template, request, send_file, abort


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

        globs = glob.glob("*.mp3")
        filename = globs[0]

        return send_file(
            filename,
            mimetype="audio/mpeg",
            as_attachment=True,
            attachment_filename=f"{title}.mp3",
        )
    except youtube_dl.utils.DownloadError as err:
        abort(406, "URL format incorrect.")
    except Exception as err:
        abort(500)
    else:
        os.remove(filename)

    return req
