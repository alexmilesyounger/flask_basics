from flask import Flask

app = Flask(__name__)

@app.route('/') # ROUTE
@app.route('/<name>') # ALTERNATE ROUTE
def index(name="Treehouse"): # FUNCTION / VIEW
	return "Hello from {}".format(name)


@app.route('/add/<int:num1>/<int:num2>') # Add two integers
@app.route('/add/<float:num1>/<float:num2>') # Add two floats
@app.route('/add/<int:num1>/<float:num2>') # Add one integer and one float
@app.route('/add/<float:num1>/<int:num2>') # Add one float and one integer

def add(num1, num2):

	return """
	<html>
	<head><title>Adding:</title></head>
	<body>
	<h1>{} + {} = {}</h1>
	</body>
	</html>
	""".format(num1, num2, num1 + num2) # return string

# RUN
app.run(debug=True)
# app.run(debug=True, port=8000, host='0.0.0.0') # for treehouse
