# mlbadminton

## Project Overview
In this project, I'll use an IMU (Inertial Measurement Unit) and Machine Learning to classify and learn to differentiate between three badminton swings: the **smash**, the **clear**, and the **drop**. I'll also be developing my skills in data handling/visualization. I'm hoping to leverage my physical understanding of badminton swing mechanics and also pattern recognition to perform feature engineering, resulting in dimension reduction and enhanced model training.

## Required Items
- Badminton racket
- Witmotion BWT61

## Goals
- **Gather data** for all types of swings
- Use pandas and numpy to **clean the data**
- **Visualize the data** using matplotlib and **observe patterns**
- Leverage physical intuition and pattern recognition to **extract features**
- **Train different models** using scikit-learn, keeping in mind good practices such as k-fold cross validation
- **Calculate success rates** for various situations (different models, amount of swing data, extracted features or lack thereof, etc)
- **Compare and evaluate models** for these situations
- **Make educated conclustions** based on model evaluations

## Current and Past Steps
- [x] Gather around 50 swings for each swing type
- [x] Add raw CSV files into [raw_csv](https://github.com/ChoongGao/mlbadminton/tree/master/raw_csv) using [pull_data](https://github.com/ChoongGao/mlbadminton/blob/master/pull_data.py)
- [x] Visualize data for swing types with [peek_data](https://github.com/ChoongGao/mlbadminton/blob/master/peek_data.py) using matplotlib (sample visualization shown below, more can be found in [images](https://github.com/ChoongGao/mlbadminton/tree/master/images))
![Sample Visualization](https://github.com/ChoongGao/mlbadminton/blob/master/images/angular_velocity.png)
- [x] Use data visualization to observe patterns and find significant features
- [x] Convert raw CSV files to raw dataframes using Pandas
- [x] Refine the dataframes and extract features into arrays of significantly smaller dimension using [extract_features](https://github.com/ChoongGao/mlbadminton/blob/master/extract_features.py)
- [x] Train models with 5-fold cross validation using the extracted features with [train_models](https://github.com/ChoongGao/mlbadminton/blob/master/train_models.py)
- [x] Trained models: **logistic regression**, **k-nearest neighbors**, **random forest**
- [x] Calculate the success rate of different models

## Next steps
- [ ] Train more models of different types (ex: neural networks)
- [ ] Perform further analysis of data and try extracting other features
- [ ] Calculate the success rates of models when given various amounts of data
- [ ] Calculate the success rates of models when different features are extracted
- [ ] Calculate the success rates of models when raw data is given (no feature extraction)
- [ ] Compare the models and make conclusions
