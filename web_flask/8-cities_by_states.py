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


@app.route('/cities_by_states')
def states_list():
    all_states = storage.all(State)
    sorted_states = sorted(all_states.values(), key=lambda state: state.name)

    return render_template("8-cities_by_states.html", states=sorted_states)


@app.teardown_appcontext
def teardown(td):
    storage.close()


if __name__ == "__main__":
    app.run()
