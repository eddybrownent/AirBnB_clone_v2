#!/usr/bin/python3
"""
This script  that starts a Flask web application
listening on 0.0.0.0, port 5000
"""

from flask import Flask

""" Creating a Flask web application instance """
app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns a response when the root URL is accessed """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Return a response when the "/hbnb" route is accessed """
    return "HBNB"


if __name__ == "__main__":
    """ Run the Flask application """
    app.run(host='0.0.0.0', port=5000)
