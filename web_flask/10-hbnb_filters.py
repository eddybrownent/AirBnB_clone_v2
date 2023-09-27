#!/usr/bin/python3
"""Starts a Flask web application"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main HBnB filters HTML page."""

    state_cities_dict = {}
    states = storage.all("State").values()
    for state in states:
        if hasattr(state, 'cities'):
            state_cities_dict[state] = state.cities
    amenities = storage.all("Amenity").values()
    return render_template("10-hbnb_filters.html",
                           state_cities_dict=state_cities_dict,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
