# PULLS ALL DATA FROM THE IMU DIRECTORY, ELIMINATES IRRELEVANT BUFFER, AND MOVES IT TO RAW_CSV

# Imports
import os
import csv

# Constants
PATH_TO_IMU = '../../Witmotion/Data'
PATH_TO_RAW_CSV = './raw_csv'
CSV_DELIMITER = '\t' # Delimiter for raw csv file
NUM_IRR = 1 # Number of irrelevant rows at top of raw csv file to be removed
NEW_LINE = '' # Desired newline for new csv


if __name__ == '__main__':

    # Asks user which type of swing is being pulled
    while True:
        try:
            SWING_TYPE = input("Please enter the type of swing being pulled (smash, clear, drop): ")
            if SWING_TYPE not in ['smash', 'clear', 'drop']:
                raise NameError('Swing type not found, please try again')
            break
        except NameError as e:
            print(e)

    # Walks to IMU Diretory
    for root,dir,files in os.walk(PATH_TO_IMU):
        for name in files:
            # Change to csv file
            new_name = name.split('.')[0] + '.csv'
            if name == '200809160919.txt':
                # Reads in old txt, removes buffer data, saves to new csv in raw_csv
                old_txt = open(os.path.join(root, name), 'r')
                new_csv = open(os.path.join(PATH_TO_RAW_CSV, SWING_TYPE, new_name), 'w', newline='')
                csv_reader = csv.reader(old_txt, delimiter=CSV_DELIMITER)
                csv_writer = csv.writer(new_csv)
                for i, row in enumerate(csv_reader):
                    if i >= NUM_IRR:
                        csv_writer.writerow(row)
                old_txt.close()
                new_csv.close()

            