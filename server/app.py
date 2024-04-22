#!/usr/bin/env python3
from flask import Flask, make_response

app = Flask(__name__)

# '/' implies homepage...either http://127.0.0.1:5555 or http://127.0.0.1:5555/
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:text>')
def print_string(text):
    #see console/terminal
    print(text)
    #sent as response (in postman or network tab)
    return(text)

@app.route('/count/<int:num>')
def count(num):
    str = ''
    for i in range(num):
        str = str + f'{i}\n'
    return(str)

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    # if(operation=="+"):
    #     return str(num1 + num2 )
    # elif(operation=="-"):
    #     return str(num1-num2) 
    # elif(operation=="*"):
    #     return str(num1*num2 )
    # elif(operation=="div"):
    #     return str(num1/num2 )
    # elif(operation=="%"):
    #     return str(num1%num2)
    # else:
    #     return make_response({}, 406)
    
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        'div': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }

    # retrieving appropriate value 
    # saving lambda (anonymous) function in cur_lambda
    cur_lambda = operations[operation]
    # invoking lambda function and passing in params
    # num1 will be x, num2 will be y
    final = cur_lambda(num1, num2)
    return str(final)


if __name__ == '__main__':
    #run our app when we execute app.py 
    app.run(port=5555, debug=True)

