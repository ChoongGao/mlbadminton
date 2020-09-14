# WILL TRAIN MODELS USING EXTRACTED FEATURES

# Imports
import os
import pandas as pd
import numpy as np
from sklearn import model_selection, linear_model, neighbors

# Constants
PATH_TO_TRAINING_DIRECTORY = './extracted_data' # Path to training data
DATA_NAME = 'initial_training.csv' # Name of training data to access
SWING_TYPES = ['smash', 'drop', 'clear'] # List of the possible swing types
SWING_TO_INT = {'smash': 0, 'drop': 1, 'clear': 2} # Mapping of swing types to integer representation
NUM_SPLITS = 5 # Number of splits/folds for model training

if __name__ == '__main__':

    # Load training data into numpy array
    df = pd.read_csv(os.path.join(PATH_TO_TRAINING_DIRECTORY, DATA_NAME), index_col=0)
    matrix = df.to_numpy()

    # Separate array into labels and data
    y = matrix[:,0]
    X = matrix[:,1:]

    # Train and score models using cross validation
    k_fold = model_selection.KFold(n_splits=NUM_SPLITS, shuffle=True)
    # Will track scoring of different models
    logistic_scores = 0
    neighbor_scores = 0
    for train_index, test_index in k_fold.split(X):
        # Splits into training and testing data
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # Training logistic regression model
        log_model = linear_model.LogisticRegression()
        log_model.fit(X_train, y_train)
        logistic_scores += log_model.score(X_test, y_test)

        # Training k nearest neighbor model
        nei_model = neighbors.KNeighborsClassifier(n_neighbors=10)
        nei_model.fit(X_train, y_train)
        neighbor_scores += nei_model.score(X_test, y_test)

    # Calculates average score of models
    avg_log_score = logistic_scores/NUM_SPLITS
    avg_nei_score = neighbor_scores/NUM_SPLITS

    # Display results
    print('Average success rate of logistic regression model: {}%'.format(avg_log_score*100))
    print('Average success rate of k nearest neighbors model: {}%'.format(avg_nei_score*100))