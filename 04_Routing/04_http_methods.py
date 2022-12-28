from flask import Flask, request

# Instance of class Flask, the WSGI application
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.get('/signup')
def signup_get():
    return show_the_login_form()

@app.post('/signup')
def signup_post():
    return do_the_login()

def do_the_login():
    return 'doing the login'

def show_the_login_form():
    return 'showing the login form'