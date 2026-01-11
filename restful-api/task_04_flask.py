#!/usr/bin/python3
"""Simple API code (Python with Flask)"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
