from flask import Flask
from flask import flash
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
import json
from options import DEFAULTS

app = Flask(__name__)
app.secret_key = 'vKuqEUNvdn8YNH4A8KsVchHeNNEBKM'

def get_saved_data():
	try:
		data = json.loads(request.cookies.get('character'))
	except TypeError:
		data = {}
	return data

@app.route("/")
def index():
	return render_template(
		"index.html", 
		saves=get_saved_data()
		)

@app.route("/builder")
def builder():
	return render_template(
		"builder.html", 
		saves=get_saved_data(),
		options=DEFAULTS
		)

@app.route('/save', methods=['POST'])
def save():
	# flash messages send tiny short-term messages to users.
	flash("Alright! That looks awesome!")
	response = make_response(redirect(url_for('builder')))
	data = get_saved_data()
	data.update(dict(request.form.items()))
	response.set_cookie(
		'character', 
		json.dumps(data)
		)
	return response

app.run(debug=True)