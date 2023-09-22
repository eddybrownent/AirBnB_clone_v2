#!/usr/bin/python3
"""
This script starts a Flask web application
listening on 0.0.0.0, port 5000 and displays a text
"""

from flask import Flask

"""creating a Flask app"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


if __name__ == "__main__":
    """ Runs the Flask app on 0.0.0.0 port 5000 """
    app.run(host='0.0.0.0', port=5000)
