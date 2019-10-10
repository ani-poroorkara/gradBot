import re
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import sklearn
import io
import requests
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import pickle
import os.path


#Dataset Analysis
dataset = pd.read_csv("dataset/graddata2.csv")
print(type(dataset))
print(dataset.head())
print(dataset.shape)
print(dataset.info())
print(dataset.sum())
print(dataset.describe())
print(dataset.mean())
print(dataset.median())

#splitting input and output | splitting training & testing
dataArray = dataset.values
X = dataArray[:,1:8]
y = dataArray[:,0:1]
validation_size = 0.10
seed = 9
X_train, X_test, Y_train, Y_test = train_test_split(X,y,test_size=validation_size, random_state = seed)


#create prediction model and predict
model = LogisticRegression()
model.fit(X_train, Y_train)
predictions = model.predict(X_test)
print("Accuracy: {} ".format(accuracy_score(Y_test,predictions) * 100))
print(classification_report(Y_test, predictions))

#save model
pkl_filename = "model/pickle_model.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(model, file)