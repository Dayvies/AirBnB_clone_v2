#!/usr/bin/python3
"""Flask app"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

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
    return (render_template('7-states_list.html', dict2=dict2))


@app.route('/cities_by_states/', strict_slashes=False)
def cities_by_states():
    """show all states and their cities"""
    dict2 = {}
    for k, v in storage.all(State).items():
        dict3 = {}
        for item in v.cities:
            dict3.update({item.name: item.id})
        dict2.update({v.name: [v.id, dict3]})
    return (render_template('8-cities_by_states.html', dict2=dict2))


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """show states or city states with id"""
    dict2 = {}
    if id is None:
        for k, v in storage.all(State).items():
            dict2.update({v.name: v.id})
        return (render_template('9-states.html', dict2=dict2, num=0))
    print(id)
    for k, v in storage.all(State).items():
        if v.id == id:
            dict3 = {}
            for item in v.cities:
                dict3.update({item.name: item.id})
            dict2.update({v.name: [v.id, dict3]})
            return (render_template('9-states.html', dict2=dict2, num=1))
    return (render_template('9-states.html', dict2=dict2, num=2))


@app.route('/hbnb_filters/', strict_slashes=False)
def hbnb_filters():
    """integrate with hbnb pages"""
    dict2 = {}
    dict4 = {}
    for k, v in storage.all(State).items():
        dict3 = {}
        for item in v.cities:
            dict3.update({item.name: item.id})
        dict2.update({v.name: [v.id, dict3]})
    for k, v in storage.all(Amenity).items():
        dict4.update({v.name: v.id})
    return (render_template('10-hbnb_filters.html', dict2=dict2, dict4=dict4))


@app.route('/hbnb/', strict_slashes=False)
def hbnb():
    """integrate with hbnb pages"""
    dict2 = {}
    dict4 = {}
    dict5 = {}
    dict6 = {}
    for k, v in storage.all(State).items():
        dict3 = {}
        for item in v.cities:
            dict3.update({item.name: item.id})
        dict2.update({v.name: [v.id, dict3]})
    for k, v in storage.all(Amenity).items():
        dict4.update({v.name: v.id})
    for k, v in storage.all(Place).items():
        dict5.update({v.name: v})
    for k, v in storage.all(User).items():
        dict6.update({v.id: v})

    return (render_template('100-hbnb.html', dict2=dict2, dict4=dict4, dict5=dict5, dict6=dict6))


@ app.teardown_appcontext
def shutdown_session(exception=None):
    """end session of db"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
