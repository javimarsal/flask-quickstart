from flask import Flask, request

app = Flask(__name__)

registered_username = 'Javier'
registered_password = '1234'

# @app.route('/login/', methods=['POST', 'GET'])
# def login_post():
#     if request.method == 'POST':
#         # request_username = request.form['username']
#         # request_password = request.form['password']

#         request_username = request.args.get('username')
#         request_password = request.args.get('password')
#         print(request_username)
#         print(request_password)

#         if valid_login(request_username, request_password):
#             return 'Successful login'
        
#         return 'Invalid login'
#     return '"GET" request'

@app.post('/login/')
def login():
    request_method = request.method
    request_is_json = request.is_json
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

# def login_post():
#     print(request.method)

#     request_username = request.args.get('username')
#     request_password = request.args.get('password')

#     if valid_login(request_username, request_password):
#         return 'Successful login'
    
#     return 'Invalid login'

def valid_login(username='', password=''):
    return username == registered_username and password == registered_password
