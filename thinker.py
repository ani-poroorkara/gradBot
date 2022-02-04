import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import pickle

"""
Method: Data Processing
"""
def dataprocessing():
    dataset = pd.read_csv("data/graddata2.csv")
    print(type(dataset))
    print(dataset.head())
    print(dataset.shape)
    print(dataset.info())
    print(dataset.sum())
    print(dataset.describe())
    print(dataset.mean())
    print(dataset.median())

    dataArray = dataset.values
    X = dataArray[:,1:8]
    y = dataArray[:,0:1]

    validation_size = 0.10
    seed = 9
    X_train, X_test, Y_train, Y_test = train_test_split(X,y,test_size=validation_size, random_state = seed)

    return X_train, X_test, Y_train, Y_test

"""
Method: Creating the model

"""
def create_model(X_train, X_test, Y_train, Y_test):

    model = LogisticRegression()
    model.fit(X_train, Y_train)
    predictions = model.predict(X_test)
    print("Model --- LogisticRegression")
    print("Accuracy: {} ".format(accuracy_score(Y_test,predictions) * 100))
    print(classification_report(Y_test, predictions))

    return model

"""
Method: Testing the model
Parameters: 
    1. new_data : list of arrays
    2. model
"""
def test_model(new_data, model):

    new_array = np.asarray(new_data)
    labels = ["reject","admit"]

    prediction = model.predict(new_array)

    no_of_test_cases, cols = new_array.shape

    for i in range(no_of_test_cases):
        print("Status of Student with GRE scores = {}, GPA grade = {}, Toefl = {} , Rank = {}, Research = {}, SOP = {}, LOR = {} will be ----- {}".format(new_data[i][0],new_data[i][1],new_data[i][2],new_data[i][3],new_data[i][4],new_data[i][5],new_data[i][6], labels[int(prediction[i])]))

"""
Method: Save Model
"""
def save_model(model):
    pkl_filename = "model/pickle_model.pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(model, file)

if __name__ == "__main__":
    X_train, X_test, Y_train, Y_test = dataprocessing()
    model = create_model(X_train, X_test, Y_train, Y_test)
    test_model([(330,9,115,2,1,4,4)], model)
    save_model(model)
    print("End!")