from flask import Flask

# Instance of class Flask, the WSGI application
app = Flask(__name__)

# route() decorator
@app.route("/")
def hello_flask():
    return "<p>Hello Flask!</p>"
