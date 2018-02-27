
"""
created on Thru 26-Jan-2018 03:05:29 IST
@author: zameer ul haque and shantam vijayputra

"""

#importing Libraries.
import os,numpy,scipy,pickle,math

#creating classmethod.
class score(object):
	
	#initialisation.
	def __init__(self,clf=None):
		self.clf=clf
	
	#using classmethod and loading the data.
	@classmethod
	def load_data(self,path):

		if len(path) == 0:

			print("Path not provided")
			return self.load_data()
		else:
			clf = pickle.load(open(path,'rb'))
			return clf

	#using classmethod and getting user input data.
	@classmethod
	def get_input(self):
	
		inputs = float(input("PLease enter the GPA to predict the SAT score:").strip())

		if  inputs > 5.0 or inputs < 0.0 :

			print("Error:{}".format("GPA must be within 0.0 - 5.0"))
			return self.get_input()

		else:
			return inputs

	
	#using classmethod and displaying the data.
	@classmethod
	def dsp_data(self,predicted_data):

		print("The Predicted SAT score is :{}".format(math.ceil(predicted_data)))
		return


if __name__ == "__main__":

	#taking care of any exception cases.
	try:
		print(__doc__)
		#creating a class object.	
		obj = score()

		#loading the pickel data of the pre trained classifier.
		clf = obj.load_data("sat_score.sav")

		#getting inputs from the user.
		inputs = obj.get_input()

		#getting predictions from the classifier
		predicted_data = clf.predict(inputs)

		#displaying the predicted data.
		obj.dsp_data(predicted_data[0][0])#in case of linear regression else no need of vector scaling
	
	except Exception as e:
		
		print("Error caught :{}".format(str(e)))


