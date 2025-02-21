#!/usr/bin/python3
"""Starts flask app and routes two requests

    Returns:
        string: normal strings
    """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c(text=None):
    return "C " + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>')
def number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html',
                               number=n, even_odd="even")
    else:
        return render_template('6-number_odd_or_even.html',
                               number=n, even_odd="odd")


if __name__ == "__main__":
    app.run()
