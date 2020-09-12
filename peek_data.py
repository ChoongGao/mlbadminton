# WILL TAKE A VISUAL LOOK AT DATA FROM SMASH, DROP, OR CLEAR

# Imports
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
PATH_TO_RAW_CSV = './raw_csv'
NUM_POINTS = 100


if __name__ == '__main__':

    # Asks user how many of each swing type to peek at
    while True:
        try:
            NUM_EACH = int(input("Please enter the number of each swing you would like to peek: "))
            if NUM_EACH < 0:
                raise NameError('Please enter an integer above 0')
            break
        except NameError as e:
            print(e)
        except ValueError as e:
            print('Please enter only integers')


    # Goes through each swing 
    sampled_swings = {}
    for SWING_TYPE in ['smash', 'drop', 'clear']:
        swing_list = []
        for root,dir,files in os.walk(os.path.join(PATH_TO_RAW_CSV, SWING_TYPE)):
            for name in files:
                swing_list.append(os.path.join(root, name))
        sample = np.random.choice(np.array(swing_list), size=NUM_EACH, replace=False)
        sampled_swings[SWING_TYPE] = sample
    
    # Converts samples to dataframes
    sampled_df = {}
    for SWING_TYPE in sampled_swings:
        df_list = []
        for SWING_PATH in sampled_swings[SWING_TYPE]:
            df = pd.read_csv(SWING_PATH)
            sub_df = df[['wx(deg/s)', 'wy(deg/s)', 'wz(deg/s)']][:NUM_POINTS]
            df_list.append(sub_df)
        sampled_df[SWING_TYPE] = df_list

    
    # Plots the sampled swings
    for SWING_TYPE in sampled_swings:
        print(SWING_TYPE)
        x = np.arange(0, NUM_POINTS)
        for df in sampled_df[SWING_TYPE]:
            arr = df.to_numpy()
            plt.figure()
            plt.plot(x, arr[:,0], label='wx(deg/s)')
            plt.plot(x, arr[:,1], label='wy(deg/s)')
            plt.plot(x, arr[:,2], label='wz(deg/s)')
            plt.legend()
            plt.show()
            plt.close()
        
