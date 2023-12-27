from flask import Flask, render_template, request, make_response, session, redirect, url_for, request, abort, jsonify
from lab1 import lab1

from lab8 import lab8
from lab9 import lab9

app = Flask(__name__)

app.secret_key = '123'

app.register_blueprint(lab8)
app.register_blueprint(lab1)
app.register_blueprint(lab9)

@app.route("/")
def start():
    if 'username' in session:  # If the user is already logged in
        return redirect(url_for('main'))
    else:
        return redirect(url_for('login'))  # Redirect to the login page if not logged in



