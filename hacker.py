#!/usr/bin/env python

import flask


app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('hacker.html')

if __name__ == '__main__':
    app.run(port=5001)
