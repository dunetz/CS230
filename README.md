CS230 Project: Mid-Price Prediction for a Limit Order Book. 

The repository contains the following folders:
1. Code - contains 2 jupyter notebooks that perform data analysis and apply baseline classifiers including: logistic regression, random forests, SVM and feed forward neural network.
2. Data - contains the FI2010 data set where each days' data is in a separate zip file.
3. Input - contains classes for retrieving data from zip files and for iterators that generates batches of sequence data.
4. Model - contains classes for generating a keras model from a config file and for training the model using data generated from iteraters.
5. Papers - reference articles

Jupyter notebooks performing price change direction prediction using LSTM models are at the top level. Model parameters are stored in config files.
