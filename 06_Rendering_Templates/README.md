# Rendering Templates

Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the HTML escaping on your own to keep the application secure. Because of that Flask configures the [Jinja2](https://palletsprojects.com/p/jinja/) template engine for you automatically.

Templates can be used to generate any type of text file. For web applications, you’ll primarily be generating HTML pages, but you can also generate markdown, plain text for emails, any anything else.

For a reference to HTML, CSS, and other web APIs, use the [MDN Web Docs](https://developer.mozilla.org/en-US/).

To render a template you can use the `render_template()` method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments. Here’s a simple example of how to render a template:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

Flask will look for `templates` in the templates folder. So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your package:

**Case 1**: a module:

```
/application.py
/templates
    /hello.html
```

**Case 2**: a package:

```
/application
    /__init__.py
    /templates
        /hello.html
```

For templates you can use the full power of Jinja2 templates. Head over to the official [Jinja2 Template Documentation](https://jinja.palletsprojects.com/en/3.1.x/templates/) for more information.

Here is an example template:

```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

Inside templates you also have access to the [config](https://flask.palletsprojects.com/en/2.2.x/api/#flask.Flask.config), [request](https://flask.palletsprojects.com/en/2.2.x/api/#flask.request), [session](https://flask.palletsprojects.com/en/2.2.x/api/#flask.session) and [g](https://flask.palletsprojects.com/en/2.2.x/api/#flask.g) objects as well as the [url_for()](https://flask.palletsprojects.com/en/2.2.x/api/#flask.url_for) and [get_flashed_messages()](https://flask.palletsprojects.com/en/2.2.x/api/#flask.get_flashed_messages) functions.

Templates are especially useful if inheritance is used. If you want to know how that works, see [Template Inheritance](https://flask.palletsprojects.com/en/2.2.x/patterns/templateinheritance/). Basically template inheritance makes it possible to keep certain elements on each page (like header, navigation and footer).