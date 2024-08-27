#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    #return an instance of a response
    #return jsonify({}), 200
    # this will also return an instance of a response, traditionally used with Flask views (the front-end portion of Flask)
    # however we will not be using Flask views, we will be using React for our front-end
    #return make_response({}, 200)
    # this IS NOT an instance of a response, this is an instance of a dictionary
    #return {}, 200

    return make_response('<h1>Python Operations with Flask Routing and Views</h1>', 200)

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return make_response(parameter, 200)

@app.route('/count/<int:parameter>')
def count(parameter):
    new_str = ''
    for i in range(0, parameter):
        new_str += str(f'{i}\n')
    return make_response(new_str, 200)

# CANNOT RETURN INTEGERS AS RESPONSE, convert to string
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    import ipdb; ipdb.set_trace()
    if(operation == '+'):
        return make_response(str(num1 + num2), 200)
    elif(operation == '-'):
        return make_response(str(num1 - num2), 200)
    elif(operation == '*'):
        return make_response(str(num1 * num2), 200)
    elif(operation == 'div'):
        return make_response(str(num1/num2), 200)
    elif(operation == '%'):
        return make_response(str(num1%num2), 200)
    else:
        #unprocessable entity, error handling for invalid characters
        return make_response({"error": "something went wrong"}, 422)
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
