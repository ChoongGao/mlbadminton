# WILL TRAIN MODELS USING EXTRACTED FEATURES

# Imports
import os
import pandas as pd
import numpy as np
from sklearn import model_selection, linear_model, neighbors

# Constants
PATH_TO_TRAINING_DIRECTORY = './extracted_data' # Path to raw csv data
DATA_NAME = 'initial_training.csv'
SWING_TYPES = ['smash', 'drop', 'clear'] # List of the possible swing types
SWING_TO_INT = {'smash': 0, 'drop': 1, 'clear': 2}
AXES = ['x', 'y', 'z']
NUM_END = 1


if __name__ == '__main__':

    # Load training data into numpy array
    df = pd.read_csv(os.path.join(PATH_TO_TRAINING_DIRECTORY, DATA_NAME), index_col=0)
    matrix = df.to_numpy()

    # Separate array into labels and data
    y = matrix[:,0]
    X = matrix[:,1:]

    k_fold = model_selection.KFold(shuffle=True)
    logistic_scores = 0
    for train_index, test_index in k_fold.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # log_model = linear_model.LogisticRegression()
        # log_model.fit(X_train, y_train)

        nei_model = neighbors.KNeighborsClassifier(n_neighbors=10)
        nei_model.fit(X_train, y_train)
        print(nei_model.score(X_test, y_test))