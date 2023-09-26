#!/usr/bin/python3
"""
Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states: Display a list of all State objects sorted by name.
    /states/<id>: Display a list of cities in a specific State.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

""" Creating a Flask web application instance """
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Display a list of all State objects sorted by name.
    """
    state_list = []
    states = storage.all("State").values()
    for state in states:
        if isinstance(state, State):
            state_list.append(state)
    return render_template('9-states.html', mode='all', state_list=state_list)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """
    Display a list of cities in a specific State.
    """
    state_list = []
    states = storage.all("State").values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html',
                                   state_list=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


@app.teardown_appcontext
def teardown(exc):
    """
    Remove the current SQLAlchemy session.
    """
    storage.close()


if __name__ == "__main__":
    """ Runs the Flask app """
    app.run(host="0.0.0.0", port=5000)
