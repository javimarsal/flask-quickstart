# Routing

## Variable Rules

You can add variable sections to a URL by marking sections with `<variable_name>`. Your function then receives the `<variable_name>` as a keyword argument. Optionally, you can use a converter to specify the type of the argument like `<converter:variable_name>`.

```python
from flask import Flask
from markupsafe import escape

# Instance of class Flask, the WSGI application
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {escape(post_id)}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
```

Converter types:

| Converter | Description |
|-----------|-------------|
|`string`   | (default) accepts any text without a slash |
| `int`     | accepts positive integers |
| `float`   | accepts positive floating point values |
| `path`     | like `string` but also accepts slashes |
| `uuid`     | accepts UUID strings |

## Unique URLs / Redirection Behaviour

The following two rules differ in their use of a trailing slash `/`.

```python
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return f'The about page'
```

The canonical URL for the projects endpoint has a trailing slash. It's similar to a folder in a file system. If you access the URL without a trailing slash (`/projects`), Flask redirects you to the canonical URL with the trailing slash (`/projects/`).

The canonical URL for the about endpoint does not have a trailing slash. It's similar to the pathname of a file. Accessing the URL with a trailing slash (`/about/`) produces a 404 "Not Found" error. This helps keep URLs unique for these resources, which helps search engines avoid indexing the same page twice.