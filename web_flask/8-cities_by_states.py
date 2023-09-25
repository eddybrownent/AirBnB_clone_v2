#!/usr/bin/python3
"""
script that starts a Flask web application
listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """
    Method to close the session
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Displays an HTML page with states and cities
    """
    state_list = storage.all(State).values()

    for state in state_list:
        return render_template('8-cities_by_states.html',
                               state_list=state_list)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
