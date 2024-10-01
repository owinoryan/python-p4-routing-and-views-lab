#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# 1. Index view at base URL "/"
@app.route('/')
def index():
    # Display the title in <h1> tags
    return '<h1>Python Operations with Flask Routing and Views</h1>'  

# 2. print_string view to print and display a given string
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print to the console
    return parameter  # Return plain text instead of <h1> tags

# 3. count view to display numbers up to a given integer
@app.route('/count/<int:parameter>')
def count(parameter):
    # Generate numbers from 0 to (parameter - 1) and display each on a new line
    # Join the numbers with "\n" to create a new line-separated string
    numbers = "\n".join(str(i) for i in range(parameter))
    return f'{numbers}\n'

# 4. math view to perform basic arithmetic operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    # Perform arithmetic based on the given operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Unsupported operation"
    
    # Return the result as plain text
    return str(result)

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
