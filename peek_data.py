# WILL TAKE A VISUAL LOOK AT DATA FROM SMASH, DROP, OR CLEAR

# Imports
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
PATH_TO_RAW_CSV = './raw_csv' # Path to raw csv data
NUM_POINTS = 120 # Num entries for each data type to include
SWING_TYPES = ['smash', 'drop', 'clear'] # List of the possible swing types
DATA_TYPE = '' # Initial of the data type the user wants to peek
DATA_TYPE_TO_COLUMNS = {'a': ['ax(g)', 'ay(g)', 'az(g)'], 'v': ['wx(deg/s)', 'wy(deg/s)', 'wz(deg/s)'], 'A': ['ax(g)', 'ay(g)', 'az(g)'], 'V': ['wx(deg/s)', 'wy(deg/s)', 'wz(deg/s)']} # Maps user input to headers of corresponding data


if __name__ == '__main__':

    # Asks user how many of each swing type to peek at, takes in values from 1-3 for ease of view
    while True:
        try:
            NUM_EACH = int(input("Please enter the number of each swing you would like to peek (1-3): "))
            if NUM_EACH < 0 or NUM_EACH > 3:
                raise NameError('Please enter an integer above 0 and below 4')
            break
        except NameError as e:
            print(e)
        except ValueError as e:
            print('Please enter only integers')

    # Asks user to look at acceleration or angular velocity
    while True:
        try:
            DATA_TYPE = (input("Would you like to compare acceleration (a) or angular velocity (v)? "))
            if DATA_TYPE not in ['a', 'v', 'A', 'V']:
                raise NameError('Please choose either \'a\' or \'v\'')
            break
        except NameError as e:
            print(e)

    # Goes through each swing
    sampled_swings = {}
    for swing_type in SWING_TYPES:
        swing_list = []
        # Adds every swing of the swing type into a list
        for root,dir,files in os.walk(os.path.join(PATH_TO_RAW_CSV, swing_type)):
            for name in files:
                swing_list.append(os.path.join(root, name))
        # Randomly samples from the list without replacement
        sample = np.random.choice(np.array(swing_list), size=NUM_EACH, replace=False)
        # Adds the sampled swings to the dictionary under the swing type
        sampled_swings[swing_type] = sample
    
    # Converts samples to dataframes
    sampled_df = {}
    for swing_type in SWING_TYPES:
        df_list = []
        for SWING_PATH in sampled_swings[swing_type]:
            df = pd.read_csv(SWING_PATH)
            # Reads in the data that the user requested
            sub_df = df[DATA_TYPE_TO_COLUMNS[DATA_TYPE]][:NUM_POINTS]
            df_list.append(sub_df)
        # Adds the swings to the dictionary of swings and pairs to the swing type
        sampled_df[swing_type] = df_list


    # Plots the sampled swings
    fig = plt.figure(figsize=(8, 8))
    fig.subplots_adjust(hspace=0.4, wspace=0.4)
    labels = DATA_TYPE_TO_COLUMNS[DATA_TYPE]
    # Iterates through different swing types
    for row, swing_type in enumerate(SWING_TYPES):
        x = np.arange(0, NUM_POINTS)
        # Iterates through the swings of the current type
        for col, df in enumerate(sampled_df[swing_type]):
            arr = df.to_numpy()
            sub = fig.add_subplot(len(SWING_TYPES), NUM_EACH, (row*NUM_EACH)+col+1)
            # Plots the data in the dataframe
            plt.plot(x, arr[:,0], label=labels[0])
            sub.plot(x, arr[:,1], label=labels[1])
            sub.plot(x, arr[:,2], label=labels[2])
            sub.title.set_text(swing_type + ' ' + str(col+1))
            sub.legend(loc='lower left', fontsize='xx-small')
    # Show the figure
    plt.show()