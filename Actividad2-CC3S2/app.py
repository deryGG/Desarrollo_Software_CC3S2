import os
from flask import Flask, jsonify
import logging

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 8080))
MESSAGE = os.environ.get("MESSAGE", "Hola CC3S2")
RELEASE = os.environ.get("RELEASE", "v1")

logging.basicConfig(level=logging.INFO)

@app.route("/", methods=["GET"])
def index():
    app.logger.info(f"Mensaje: {MESSAGE}, Release: {RELEASE}")
    return jsonify({"message": MESSAGE, "release": RELEASE})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)