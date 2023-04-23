#!/usr/bin/python3
"""Starts a flask app and renders list of states

    Returns:
        file: Contains list of states
    """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    all_states = storage.all(State)
    sorted_states = sorted(all_states.values(), key=lambda state: state.name)

    return render_template("9-states.html",
                           states=sorted_states, present="all")


@app.route('/states/<id>')
def state_id(id):
    all_states = storage.all(State)
    for state in all_states.values():
        if id == state.id:
            return render_template("9-states.html",
                                   states=state, present="one")
    return render_template("9-states.html", states="", present="")


@app.teardown_appcontext
def teardown(td):
    storage.close()


if __name__ == "__main__":
    app.run()
