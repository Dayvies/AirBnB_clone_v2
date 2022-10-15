#!/usr/bin/python3
"""Flask app"""

from flask import Flask, render_template
from models import storage
from models.state import State
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


@app.route('/states_list/', strict_slashes=False)
def states_list():
    """show all states"""
    dict2 = {}
    for k, v in storage.all(State).items():
        dict2.update({v.name: v.id})
    print(dict2)
    return (render_template('7-states_list.html', dict2=dict2))


@app.teardown_appcontext
def shutdown_session(exception=None):
    """end session of db"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
