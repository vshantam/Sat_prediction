# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:49:37 2018

@author: Shantam Vijayputra and Zameer Ul Haque
"""

#importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Imputer
from sklearn.linear_model import LinearRegression
import pickle
from mlxtend.plotting import plot_learning_curves
from mlxtend.preprocessing import shuffle_arrays_unison
from sklearn import tree
import math

#import math

#creating class model
class sat(object):

    def __init__ (self,df=None):
        
        self.df = df

    #using classmethod and loading the dataset
    @classmethod
    def load_data(self,path):
        
        df = pd.read_csv(path);
        x = df.iloc[:,0].values.reshape(-1,1)
        y = df.iloc[:,1].values.reshape(-1,1)

        return x,y

    #using classmethod and splitting the training and testing dataset
    @classmethod
    def split(self,x,y):
        
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
        return x_train, x_test, y_train, y_test

    #using classmethod and scaling the feautues may or may not be necessary based on quality of the dataset
    @classmethod
    def scale(self,x_train, x_test, y_train, y_test):
        
        sc = StandardScaler()
        x_train = sc.fit_transform(x_train)
        x_test = sc.fit_transform(x_test)
        y_test = sc.fit_transform(y_test)
        y_train = sc.fit_transform(y_train)

        return x_train, x_test, y_train, y_test

    #using classmethod and taking care of missing values using imputer
    @classmethod
    def missing_val(self,x_train):

        imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
        imputer = imputer.fit(x_train[:, :])
        x_train[:, :] = imputer.transform(x_train[:, :])

        return x_train
    

    #using classmethod and defining classifier
    @classmethod
    def classifier(self):
        
        clf = tree.DecisionTreeClassifier()
        #clf = LinearRegression()

        return clf
    

    #using classifier and plotting the data
    # Visualising the Test set results

    @classmethod
    def plot(self,clf,x,y,color1,color2,title,xlable,ylable):
        
        plt.scatter( x, y, color = color1 )
        plt.scatter(x, clf.predict(x), color = color2)
        plt.title(title)
        plt.xlabel(xlable)
        plt.ylabel(ylable)
        plt.legend()
        
        return plt.show()
        

    #using classmethod and saving the data
    @classmethod
    def save_classifier(self,clf,name_with_path,_type):
        
        return pickle.dump(clf, open(name_with_path, _type))

    #using classmethod and loading the data
    @classmethod
    def load_classifier(self,name_with_path,_type):

        clf = pickle.load(open(name_with_path,_type))

        return clf   

    #creating main function using classmethod
    @classmethod
    def main(self):
        
        print(__doc__)
        #creating object instances
        obj = sat()
        #extracting features and output
        x,y  = obj.load_data("gpa.csv")
        #splitting the data
        x_train,x_test,y_train,y_test = obj.split(x,y)
        #scaling the data
        #x_train,x_test,y_train,y_test = obj.scale(x_train,x_test,y_train,y_test)
        #missing value imputation
        x_train = obj.missing_val(x_train)
        x_test = obj.missing_val(x_test)
        y_train = obj.missing_val(y_train)
        y_test = obj.missing_val(y_test)
        #generating classifier
        clf = obj.classifier()
        #fitting the features into the model
        clf.fit(x_train,y_train)
        #plotting training set
        obj.plot(clf,x_train,y_train,"orange","blue","sat score (Training set)","GPA","SAT SCORE")
        #plotting the testing set
        obj.plot(clf,x_test,y_test,"orange","blue","sat score (Testing set)","GPA","SAT SCORE")
        #saving classifier
        obj.save_classifier(clf,"sat_score.pkl","wb")
        #loading the data
        clf = obj.load_classifier("sat_score.pkl","rb")
        
        x, y = shuffle_arrays_unison(arrays=[x, y], random_seed=5)

        plot_learning_curves(x_train, y_train, x, y, clf)
        plt.show()


        
if __name__ == "__main__":

    obj1 = sat()
    obj1.main()

