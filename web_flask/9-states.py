#!/usr/bin/python3
"""
This script starts a Flask web application
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def list_state_objects():
    """
    Prints HTML page
    With a list of all States
    """
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def list_state_id(id):
    """
    Prints HTML page
    With id information if present
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
        return render_template("9-states.html")


@app.teardown_appcontext
def teardown_appcontext(exc):
    """
    Closes and removes the current SQLAchemy session in the file storage
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
