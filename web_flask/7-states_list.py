#!/usr/bin/python3
"""
This script starts a Flask web application
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_state_objects():
    """
    Prints HTML page
    With a list of all state objects present in DBStorage
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_appcontext(exc):
    """
    Closes and removes the current SQLAchemy session in the file storage
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
