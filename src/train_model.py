## 
# train_model.py - Builds the training model for the predictions and saves the model to disk.
#
## 	
import pandas as pd 
import feather
from tpot import TPOT
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.cross_validation import train_test_split

path_to_processed_data = '../../data/processed/'

df = feather.read_dataframe(path_to_processed_data + 'clean_dataset.feather')

# The features and target that we will use for our analysis
features = ['ScoreDiff', 'down', 'qtr', 'yrdstogo', 'yrdline100']
target = 'PlayType'

# Since the algorithms won't understand the PassType column as is, we will map to an integer instead
df['PlayType'] = df['PlayType'].map({'Run' : 0, 'Pass': 1})

# Split the dataset into seperate test and train sets
(train_X, test_X, train_y, test_y) = train_test_split(df[features], df[target], test_size = 0.2)

tpot = TPOT(generations=5)

tpot.fit(train_X, train_y)