#!/usr/bin/env python

import logging
import os
import random

import flask


app = flask.Flask(__name__)
app.secret_key = 'SECRET_KEY'


@app.route('/')
def home():
    if not check_login():
        return flask.render_template('login.html')
    # CSRF hint: Something goes here.
    return flask.render_template('bank.html', csrf_token=None)

@app.route('/login/', methods=['POST'])
def login():
    if flask.request.form.get('password') != 'donuts':
        return flask.abort(401, 'You fail - wrong password')
    do_login()
    # CSRF hint: Something goes here.
    return flask.redirect('/')

@app.route('/send_payment/', methods=['POST'])
def send_payment():
    if not check_login():
        return flask.abort(401, 'You fail - not logged in')
    # CSRF hint: Something goes here.
    response = flask.make_response('${} sent to {}'.format(
        flask.request.form['amount'],
        flask.request.form['recipient']
    ))
    response.headers['Content-Type'] = 'text/plain'
    return response

# Auth stuff
def do_login():
    flask.session['is_logged_in'] = True

def check_login():
    return flask.session.get('is_logged_in', False)

# CSRF stuff
def set_csrf_token():
    flask.session['csrf_token'] = '{0:x}'.format(random.getrandbits(128))

def get_csrf_token():
    return flask.session['csrf_token']

def check_csrf_token(token):
    return token == get_csrf_token()

# Runs app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
