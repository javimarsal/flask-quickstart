from flask import Flask, abort, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    # error 401 => access denied
    abort(401)
    this_is_never_executed()