from flask import Flask
from markupsafe import escape

# Instance of class Flask, the WSGI application
app = Flask(__name__)

# route() decorator
@app.route("/")
def hello_flask():
    return "<p>Hello Flask!</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"