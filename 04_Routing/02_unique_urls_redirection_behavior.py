from flask import Flask

# Instance of class Flask, the WSGI application
app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return f'The about page'