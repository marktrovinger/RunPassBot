## 
# predict_model.py - Adds functionality for making predictions.
#
##
from sklearn.externals import joblib

path_to_model = '../models/'

## 
# predict_playtype - Returns an array containing the predicted playtype (Run: 0, Pass: 1)
#
##
def predict_playtype(test_X):
	gbc = joblib.load(path_to_model + 'gbc.pkl')
	return gbc.predict(test_X)

##
# predict_playtype_proba - Returns an array containing the probabilities that a play will be a Run or Pass.
#
##
def predict_playtype_proba(test_X):
	gbc = joblib.load(path_to_model + 'gbc.pkl')
	return gbc.predict_proba(test_X)
