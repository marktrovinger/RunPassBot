## 
# predict_model.py - Adds functionality for making predictions.
#
##
from sklearn.externals import joblib

path_to_model = '../models/'

## 
def predict_playtype(test_X):
	gbc = joblib.load(path_to_model + 'gbc.pkl')
	gbc.predict(test_X)
