from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
import re
import os

# setup the app
app = Flask(__name__)
app.config['DEBUG'] = True


####  setup routes  ####
@app.route('/')
def index():
    return render_template('forms.html')

@app.route('/charts', methods=["POST","GET"])
def sentiment_analysis():

    print("here")
    # get the data from our form    
    positive_score = request.form['positive']
    negative_Score = request.form['negative']
    
    print(positive_score)
    print(negative_Score)

    return render_template('charts.html')

if __name__ == "__main__":
	# change to app.run(host="0.0.0.0"), if you want other machines to be able to reach the webserver.
	app.run(host="0.0.0.0",port=5001) 