from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/') # ROUTE
@app.route('/<name>') # ALTERNATE ROUTE
def index(name="Treehouse"): # FUNCTION / VIEW
	name = request.args.get('name', name)
	return "Hello from {}".format(name)


# RUN
app.run(debug=True)
# app.run(debug=True, port=8000, host='0.0.0.0') # for treehouse
