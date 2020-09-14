# WILL EXTRACT FEATURES FROM RAW_CSV TO REFINED DATAFRAME

# Imports
import os
import pandas as pd
import numpy as np

# Constants
PATH_TO_RAW_CSV = './raw_csv' # Path to raw csv data
PATH_TO_EXTRACTED = './extracted_data/initial_training.csv' # Path where extracted features will be saved
SWING_TYPES = ['smash', 'drop', 'clear'] # List of the possible swing types
SWING_TO_INT = {'smash': 0, 'drop': 1, 'clear': 2} # Mapping of swing type to integer representation
AXES = ['x', 'y', 'z'] # Three axes that measurements come in
NUM_END = 1 # Case where final data entry is incomplete
TRAINING_HEADERS = ['Swing Type', 'MinWX', 'MaxWX', 'MinWY', 'MaxWY', 'MinWZ', 'MaxWZ', 'MinAX', 'MaxAX', 'MinAY', 'MaxAY', 'MinAZ', 'MaxAZ'] # Headers for the training dataframe
FILE_NAME = 'initial_training.csv' # Name training data will be saved as


# Takes input of the swing dataframe, outputs array of label extracted features
def extract_features(df, label):
    # Case where final data entry is incomplete
    df = df.drop(df.tail(NUM_END).index)
    # Create array and insert label
    extracted = []
    extracted.append(SWING_TO_INT[label])
    # For angular velocity, find the maximum/minimum for all three directions and append
    for direction in AXES:
        col = 'w{}(deg/s)'.format(direction)
        data = df[[col]]
        arr = data.to_numpy()
        minimum = arr.min()
        maximum = arr.max()
        extracted.append(minimum)
        extracted.append(maximum)

    # For acceleration, find the maximum/minimum for all three directions and append
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
        # Adds the path to every swing of the swing type into a list
        for root,dir,files in os.walk(os.path.join(PATH_TO_RAW_CSV, swing_type)):
            for name in files:
                swing_list.append(os.path.join(root, name))
        
        # For every swing of this type, extract the features and append to the training list
        for swing_path in swing_list:
            df = pd.read_csv(swing_path)
            extracted_swing = extract_features(df, swing_type)
            training_list.append(extracted_swing)
    
    # Transfer training data from the list to the dataframe, then save to the folder
    training_df = pd.DataFrame(data=training_list, columns=TRAINING_HEADERS)
    saved_file = open(os.path.join(PATH_TO_EXTRACTED, FILE_NAME), 'w')
    training_df.to_csv(path_or_buf=saved_file)
    saved_file.close()