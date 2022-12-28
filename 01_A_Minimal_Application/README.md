# A Minimal Application

## Import Flask

First we import the **Flask** class.

```python
from flask import Flask
```

## Create an Instance of class Flask

An instance of class Flask will be our WSGI application.
- WSGI, the standard Python interface between applications and servers

The first argument is the name of the application's module or package.

- `__name__` is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

```python
app = Flask(__name__)
```

## Routes

**route()** decorator to tell Flask what URL should trigger our function.

The function returns the message we want to display in the user's browser. The default content type is HTML, so HTML in the string will be rendered by the browser.

```python
@app.route("/")
def hello_flask():
    return "<p>Hello Flask!</p>"
```

## Run Application

To run the application, use the flask command or python -m flask
```bash
$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```



### Application Discovery Behavior

As a shortcut, if the file is named **app.py** or **wsgi.py**, you don't have to use --app. See [Command Line Interface](https://flask.palletsprojects.com/en/2.2.x/cli/) for more details.
```bash
$ flask run
```

Now head over to http://127.0.0.1:5000/, and you should see your hello world greeting.

- If another program is already using port 5000, you'll see OSError: [Errno 98] or OSError: [WinError 10013] when the server tries to start. See Address already in use for how to handle that.


### Externally Visible Server

If you run the server you will notice that the server is only accessible from your own computer, not from any other in the network. This is the default because in debugging mode a user of the application can execute arbitrary Python code on your computer.

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:

If the name of the file is app.py or wsgi.py:
```bash
$ flask run --host=0.0.0.0
```

If the file has a different name:
```bash
$ flask --app hello run --host=0.0.0.0
```

This tells your operating system to listen on all public IPs.