from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators, IntegerField
from sklearn.externals import joblib
import pandas as pd


app = Flask(__name__)

###### Preparing classifier
model_dir = '.../models/gbc.pkl'
gbc_clf = joblib.load(model_dir)

def classify(dataframe):
	return gbc_clf.predict(dataframe)



####### Flask
class RunPassBot(Form):
	


@app.route('/')
def index():
	pass
	return render_template('runpassform.html', form=form)

@app.route('/prediction')
def results():
	pass


if __name__ == '__main__':
	app.run(debug=True)