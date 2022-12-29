# Accesing Request Data

For web applications it’s crucial to react to the data a client sends to the server. In Flask this information is provided by the global **request** object. If you have some experience with Python you might be wondering how that object can be global and how Flask manages to still be threadsafe. The answer is context locals.

## The Request Object

The request object is documented in the API section and we will not cover it here in detail (see [Request](https://flask.palletsprojects.com/en/2.2.x/api/#flask.Request)). Here is a broad overview of some of the most common operations. First of all you have to import it from the `flask` module:

```python
from flask import request
```

The current request method (GET, POST, ...) is available by using the `method` attribute. To access form data (data transmitted in a POST or PUT request) you can use the form attribute. Here is a full example of the two attributes mentioned above:

```python
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
```

What happens if the key does not exist in the form attribute? In that case a special **KeyError** is raised. You can catch it like a standard **KeyError** but if you don't do that, a HTTP 400 Bad Request error page is shown instead. So for many situations you don’t have to deal with that problem.

To access parameters submitted in the URL (/?key1=value1&key2=value2) you can use the args attribute:

```python
searchword = request.args.get('key', '')
```

An more complete example using parameters submitted in the URL:

```python
@app.post('/login/')
def login_post():
    print(request.method)

    request_username = request.args.get('username')
    request_password = request.args.get('password')

    if valid_login(request_username, request_password):
        return 'Successful login'
    
    return 'Invalid login'
```

We recommend accessing URL parameters with get or by catching the [KeyError](https://docs.python.org/3/library/exceptions.html#KeyError) because users might change the URL and presenting them a 400 bad request page in that case is not user friendly.

For a full list of methods and attributes of the request object, head over to the [Request](https://flask.palletsprojects.com/en/2.2.x/api/#flask.Request) documentation.

### Read JSON from body request
How to read a POST request that contains a JSON in the body:

JSON body:

```javascript
{
  "username": "John Doe",
  "password": "1234"
}
```

Flask application:

```python
@app.post('/login/')
def login():
    # The Request method is POST
    request_method = request.method
    # True of False if the request has a json or not
    request_is_json = request.is_json

    # Retrieve the JSON from body and get the values for properties 'username' and 'password'
    request_content_json = request.get_json()
    request_username = request_content_json['username']
    request_password = request_content_json['password']

    print(request_method)
    print(request_is_json)
    print(request_username)
    print(request_password)
    
    if valid_login(request_username, request_password):
        return 'Valid login'
    
    return 'Not Valid login'
```