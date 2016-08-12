## 
# train_model.py - Builds the training model for the predictions and saves the model to disk.
#
## 	
import pandas as pd 
import feather
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.externals import joblib

path_to_processed_data = '../data/processed/'
path_to_model ='../models/'

df = feather.read_dataframe(path_to_processed_data + 'clean_dataset.feather')

# The features and target that we will use for our analysis
features = ['ScoreDiff', 'down', 'qtr', 'ydstogo', 'yrdline100']
target = 'PlayType'

# Since the algorithms won't understand the PassType column as is, we will map to an integer instead
df['PlayType'] = df['PlayType'].map({'Run' : 0, 'Pass': 1})

# Split the dataset into seperate test and train sets
(train_X, test_X, train_y, test_y) = train_test_split(df[features], df[target], test_size = 0.2)

# Create the GradientBoostingClassifier, set with the weights from TPOT, and then fit the model to the 
# dataset that we have
gbc = GradientBoostingClassifier(learning_rate=0.16, max_features=1.0, 
								 min_weight_fraction_leaf=1e-06, n_estimators=500, random_state=42)
gbc.fit(train_X, train_y)

# Save the model for later use
joblib.dump(gbc, path_to_model + 'gbc.pkl')
