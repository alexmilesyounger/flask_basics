from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
import json

app = Flask(__name__)

# function to get saved data (cookie) outside of the index view
def get_saved_data():
	# see if what is returned is something we can turn into json data
	try:
		# json dump string from the cookie named character
		# json dumps creates a json string, loads takes that string and turns it into python code
		data = json.loads(request.cookies.get('character'))
	# if we can't turn what is returned into json data
	except TypeError:
		# make data an empty dict
		data = {}
	return data


@app.route("/")
def index():
	data = get_saved_data()
	return render_template("index.html", saves=data)

@app.route('/save', methods=['POST'])
def save():
	# in Flask cookies are set on the response
	# we always need a response even if it's fake
	response = make_response(redirect(url_for('index')))
	data = get_saved_data()
	data.update(dict(request.form.items()))
	#set the cookie, name it "character", dump in the data from
	# the form, convert the immutablemultidict to a normal dict
	# dump the string "dumps" via json
	# update the cookie if anything has changed and send that back
	response.set_cookie('character', json.dumps(data))
	return response

app.run(debug=True)