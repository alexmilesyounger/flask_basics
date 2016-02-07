from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


# create a new route with a function for 
# data submitted by the form
# only accessible if you POST to it
@app.route('/save', methods=['POST'])
def save():
	import pdb; pdb.set_trace() # python debugger
	# with pdb save the form and look at the console
	# I'll see what's going on and the (Pdb) prompt will 
	# show up. From here I can look around inside the 
	# script while it's running. One of the big things
	# to look at here is Flask's request module.
	# We took a look at request.form
	# Spending some time with request would be useful.
	return redirect(url_for('index'))

app.run(debug=True)