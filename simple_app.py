from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
import twilio.twiml

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def reply_sms(reply_message="wtf?"):
	"""Respond to player with sms message."""
	resp = twilio.twiml.Response()
	# resp.sms(reply_message)
	resp.message(reply_message)
	return str(resp)

@app.route('/') # ROUTE
@app.route('/<name>') # ALTERNATE ROUTE
def index(name="Treehouse"): # FUNCTION / VIEW
	context = {'name': name}
	return render_template("index.html", **context)


@app.route('/add/<int:num1>/<int:num2>') # Add two integers
@app.route('/add/<float:num1>/<float:num2>') # Add two floats
@app.route('/add/<int:num1>/<float:num2>') # Add one integer and one float
@app.route('/add/<float:num1>/<int:num2>') # Add one float and one integer

def add(num1, num2):
	context = {'num1': num1, 'num2': num2}
	return render_template("add.html", **context)



# RUN
app.run(debug=True)
# app.run(debug=True, port=8000, host='0.0.0.0') # for treehouse
