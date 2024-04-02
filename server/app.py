#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
@app.route('/print/<string:statement>')
def print_string(statement):
    print(statement)
    return statement
@app.route('/count/<int:parameter>')
def count(parameter):
    nums =list(range(0,parameter))
    new_list = [f'{num}\n' for num in nums]
    test = "".join(new_list)
    return test
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    result = 0
    if operation == "div":
        result = (num1 / num2)
    elif operation == "+":
        result = (num1 + num2)
    elif operation == "-":
        result = (num1 -num2)
    elif operation == "*":
        result = (num1 * num2)
    return f'{result}'



if __name__ == '__main__':
    app.run(port=5555, debug=True)
