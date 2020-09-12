# WILL TAKE A VISUAL LOOK AT DATA FROM SMASH, DROP, OR CLEAR

# Imports
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Constants
PATH_TO_RAW_CSV = './raw_csv'
NUM_POINTS = 150


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
    
    

            



        