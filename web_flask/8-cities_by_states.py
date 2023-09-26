#!/usr/bin/python3
"""
This script starts a Flask wed app
listening on 0.0.0.0, port 5000
"""

from flask import Flask
from flask import render_template
from models import storage


""" Creating a Flask web application instance """
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with states and cities"""

    """ Retrieve a list of states from your database """
    states = storage.all("State").values()

    """ Create a dict to store states and their cities """
    state_cities_dict = {}

    """ Iterate through each state """
    for state in states:
        """ Check if the state has 'cities' attribute """
        if hasattr(state, 'cities'):
            """ Add the state as the key and its cities """
            state_cities_dict[state] = state.cities

    return render_template("8-cities_by_states.html",
                           state_cities_dict=state_cities_dict)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    """ Runs the Flask app """
    app.run(host="0.0.0.0", port="5000")
