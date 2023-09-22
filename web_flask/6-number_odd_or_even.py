#!/usr/bin/python3
"""
This script starts a Flask wed app
listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """ checks if n is an int """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):

    if isinstance(n, int):
        """ Render an HTML template with Number: n """
        return render_template('5-number_template.py', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even_number(n):
    """ Checks if n is integer and even or odd """
    if isinstance(n, int):
        if n % 2 == 0:
            message = "Number: {} is even".format(n)
        else:
            message = "Number: {} is odd".format(n)
        return render_template('6-number_odd_or_even.html', message=message)


if __name__ == "__main__":
    """ Runs the Flask app """
    app.run(host="0.0.0.0", port=5000)
