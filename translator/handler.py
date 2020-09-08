from googletrans import Translator
from flask import jsonify
import json


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    data = json.loads(req)
    text = data.get("text")
    dest = data.get("des") or "en"

    translator = Translator()
    translated = translator.translate(text, dest=dest, src="auto")

    return jsonify(translation=translated.text, source=translated.src, received=text)
