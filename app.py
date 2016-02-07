from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


# create a new route with a function for 
# data submitted by the form
# only accessible if you POST to it
@app.route('/save', methods=['POST'])
def save():
	return 'Saved!'

app.run(debug=True)