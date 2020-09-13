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


if __name__ == '__main__':

    # Asks user how many of each swing type to peek at
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


    # Goes through each swing 
    sampled_swings = {}
    for swing_type in SWING_TYPES:
        swing_list = []
        for root,dir,files in os.walk(os.path.join(PATH_TO_RAW_CSV, swing_type)):
            for name in files:
                swing_list.append(os.path.join(root, name))
        sample = np.random.choice(np.array(swing_list), size=NUM_EACH, replace=False)
        sampled_swings[swing_type] = sample
    
    # Converts samples to dataframes
    sampled_df = {}
    for swing_type in SWING_TYPES:
        df_list = []
        for SWING_PATH in sampled_swings[swing_type]:
            df = pd.read_csv(SWING_PATH)
            sub_df = df[['wx(deg/s)', 'wy(deg/s)', 'wz(deg/s)']][:NUM_POINTS]
            df_list.append(sub_df)
        sampled_df[swing_type] = df_list

    
    # Plots the sampled swings
    fig = plt.figure(figsize=(8, 8))
    fig.subplots_adjust(hspace=0.4, wspace=0.4)
    for row, swing_type in enumerate(SWING_TYPES):
        x = np.arange(0, NUM_POINTS)
        for col, df in enumerate(sampled_df[swing_type]):
            arr = df.to_numpy()
            sub = fig.add_subplot(len(SWING_TYPES), NUM_EACH, (row*NUM_EACH)+col+1)
            plt.plot(x, arr[:,0], label='wx(deg/s)')
            sub.plot(x, arr[:,1], label='wy(deg/s)')
            sub.plot(x, arr[:,2], label='wz(deg/s)')
            sub.title.set_text(swing_type + ' ' + str(col+1))
            sub.legend(loc='lower left', fontsize='xx-small')
    # Show the figure
    plt.savefig('Peek.png')
    plt.show()