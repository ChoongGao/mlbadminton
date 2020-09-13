# WILL EXTRACT FEATURES FROM RAW_CSV TO REFINED DATAFRAME

# Imports
import os
import pandas as pd
import numpy as np

# Constants
PATH_TO_RAW_CSV = './raw_csv' # Path to raw csv data
SWING_TYPES = ['smash', 'drop', 'clear'] # List of the possible swing types
SWING_TO_INT = {'smash': 0, 'drop': 1, 'clear': 2}
AXES = ['x', 'y', 'z']
NUM_END = 1

# Function that will take input of the swing dataframe, will output numpy array of extracted features
def extract_features(df, label):
    df = df.drop(df.tail(NUM_END).index)
    extracted = []
    extracted.append(SWING_TO_INT[label])
    for direction in AXES:
        col = 'w{}(deg/s)'.format(direction)
        data = df[[col]]
        arr = data.to_numpy()
        minimum = arr.min()
        maximum = arr.max()
        extracted.append(minimum)
        extracted.append(maximum)

    for direction in AXES:
        col = 'a{}(g)'.format(direction)
        data = df[[col]]
        arr = data.to_numpy()
        minimum = arr.min()
        maximum = arr.max()
        extracted.append(minimum)
        extracted.append(maximum)
    return extracted


if __name__ == '__main__':

    # List that contains all swings, model will be trained using this
    training_list = []

    # Goes through each swing
    sampled_swings = {}
    for swing_type in SWING_TYPES:
        swing_list = []
        # Adds every swing of the swing type into a list
        for root,dir,files in os.walk(os.path.join(PATH_TO_RAW_CSV, swing_type)):
            for name in files:
                swing_list.append(os.path.join(root, name))
        
        # For every swing of this type
        for swing_path in swing_list:
            df = pd.read_csv(swing_path)
            extracted_swing = extract_features(df, swing_type)
            training_list.append(extracted_swing)
    
    # Move all the training data from the list to the dataframe
    training_df = pd.DataFrame(data=training_list, columns=['Swing Type', 'MinWX', 'MaxWX', 'MinWY', 'MaxWY', 'MinWZ', 'MaxWZ', 'MinAX', 'MaxAX', 'MinAY', 'MaxAY', 'MinAZ', 'MaxAZ'])
    saved_file = open('./extracted_data/initial_training.csv', 'w')
    training_df.to_csv(path_or_buf=saved_file)
    saved_file.close()