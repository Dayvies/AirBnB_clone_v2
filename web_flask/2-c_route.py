#!/usr/bin/python3
"""Flask app"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """defines what to return on /"""
    return ("Hello HBNB!")


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """c/ route plus text specified"""
    text = text.replace('_', ' ')
    return ("C {}".format(text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
