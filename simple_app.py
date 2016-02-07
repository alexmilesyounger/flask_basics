from flask import Flask

app = Flask(__name__)

@app.route('/') # ROUTE
@app.route('/<name>') # ALTERNATE ROUTE
def index(name="Treehouse"): # FUNCTION / VIEW
	return "Hello from {}".format(name)


@app.route('/add/<int:num1>/<int:num2>') # Add two numbers
def add(num1, num2):
	return '{} + {} = {}'.format(num1, num2, num1 + num2) # return string

# RUN
app.run(debug=True)
# app.run(debug=True, port=8000, host='0.0.0.0') # for treehouse
