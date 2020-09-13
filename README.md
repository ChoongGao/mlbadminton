# mlbadminton

## Project Overview
In this project, I'll use an IMU (Inertial Measurement Unit) and Machine Learning to classify and learn to differentiate between three badminton swings: the **smash**, the **clear**, and the **drop**.

## Required Items
- Badminton racket
- Witmotion BWT61

## Goals
- Gather data for all types of swings
- Use pandas to format data into dataframes
- Train the model using scikit-learn
- Test the final model
- Compare and evaluate models with differing amounts of training data

## Current Steps
- [x] Gather around 50 swings for each swing type
- [x] Add raw CSV files into [raw_csv](https://github.com/ChoongGao/mlbadminton/tree/master/raw_csv) using [pull_data](https://github.com/ChoongGao/mlbadminton/blob/master/pull_data.py)
- [x] Visualize data for swing types with [peek_data](https://github.com/ChoongGao/mlbadminton/blob/master/peek_data.py) using matplotlib (sample visualization shown below)
![Sample Visualization](https://github.com/ChoongGao/mlbadminton/blob/master/Peek.png)

## Next steps
- [ ] Use data visualization to observe patterns and find significant features
- [ ] Convert raw CSV files to raw dataframes using Pandas
- [ ] Refine the dataframes and extract features into new dataframes of significantly smaller dimension
- [ ] Train various models using the refined dataframes
- [ ] Calculate the success rate of models with varying amounts of data and/or different extracted features
- [ ] Compare the models and make conclusions
