#!/usr/bin/python3
"""
This script starts a Flask wed app
listening on 0.0.0.0, port 5000
"""

from flask import Flask

""" Creating a Flask web application instance """
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns a response when root URL is accessed """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns a response when "/hbnb" route is accessed """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_display(text):
    """ Returns a response with C followed by value of text """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_display(text='is cool'):
    """ Return a response with Python and value of text """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    """ Runs the Flask app """
    app.run(host="0.0.0.0", port=5000)
