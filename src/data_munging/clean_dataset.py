##
# clean_dataset.py - Reads the dataset from /data/raw for the Run/Pass Bot and saves the final dataset
# 					 to a csv-format file in /data/processed. 	
##

import pandas as pd
import os
import glob
import feather

columns_to_remove = ['Unnamed: 0', 'Date', 'GameID', 'Drive', 'time', 'TimeUnder', 'TimeSecs',
 					'PlayTimeDiff', 'SideofField', 'yrdln','ydsnet','GoalToGo', 'FirstDown','posteam',
 					'DefensiveTeam','desc','PlayAttempted','Yards.Gained','sp','Touchdown','ExPointResult',
 					'TwoPointConv','DefTwoPoint','Safety','Passer','PassAttempt','PassOutcome','PassLength',
 					'PassLocation','InterceptionThrown','Interceptor','Rusher','RushAttempt','RunLocation','RunGap',
 					'Receiver','Reception','ReturnResult','Returner','Tackler1','Tackler2','FieldGoalResult',
 					'FieldGoalDistance','Fumble','RecFumbTeam','RecFumbPlayer','Sack','Challenge.Replay',
 					'ChalReplayResult','Accepted.Penalty','PenalizedTeam','PenaltyType','PenalizedPlayer',
 					'Penalty.Yards','PosTeamScore','DefTeamScore','AbsScoreDiff','Season']

 # TODO: path strings should be put in an env file of some kind
path_to_raw_data = '../../data/raw/'
path_to_processed_data = '../../data/processed/'

# Grab all the raw data flies from /data/raw and concat into one dataframe
all_data_files = glob.glob(os.path.join(path_to_raw_data, "*.csv"))
all_raw_dataframe = pd.concat(pd.read_csv(f) for f in all_data_files)

# Drop the columns that we don't want to use for our analysis
all_raw_dataframe.drop(columns_to_remove, inplace=True, axis=1)

# Drop the NaNs from the dataset, most of these are kickoff, timeouts, or other events we don't care about
all_raw_dataframe.dropna(inplace=True)

# For our training purposes, we only care about the run and passing plays, so we use those as a list to 
# filter our results further
play_list = ['Run', 'Pass']
final_clean_dataset = all_raw_dataframe[all_raw_dataframe['PlayType'].isin(play_list)]

# Now that we have a much cleaner dataset, we can save the dataframe to our processed data directory in
# the csv format
final_clean_dataset.to_csv(path_to_processed_data + 'clean_dataset.csv')
feather.write_dataframe(final_clean_dataset, path_to_processed_data + 'clean_dataset.feather')
