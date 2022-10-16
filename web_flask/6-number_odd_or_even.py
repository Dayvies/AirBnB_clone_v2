#!/usr/bin/python3
"""Flask app"""

from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonisfun(text="is cool"):
    """python/ route plus default text"""
    text = text.replace('_', ' ')
    return ("Python {}".format(text))


@app.route('/number/<int:n>', strict_slashes=False)
def numberOnly(n):
    """number/int routes only if end is """
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n):
    """render template if conditions are met"""
    return (render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """render template if conditions are met"""
    return (render_template('6-number_odd_or_even.html', n=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
