from rivescript import RiveScript
import os.path
import pickle
import re
import pandas as pd 
import numpy as np 
import sklearn
import io
import requests
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

#Load model
pkl_filename = "model/pickle_model.pkl"
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)

#Bot initialisation
file = os.path.dirname("__file__")
convo = os.path.join(file , 'convo')
bot = RiveScript()
bot.load_directory(convo)
bot.sort_replies()

while True:
	msg = str(input("You> "))
    
	if msg.find('gre') != -1:
		gre = [int(i) for i in msg.split() if i.isdigit()]
		print(gre)
	if msg.find('cgpa') != -1:
		cgpa = re.findall("\d+\.\d+", msg)
		cgpa = [float(i) for i in cgpa]   
		print(cgpa)
	if msg.find('toefl') != -1:
		toefl = [int(i) for i in msg.split() if i.isdigit()]
		print(toefl)
	if msg.find('rank') != -1:
		uniRank = [int(i) for i in msg.split() if i.isdigit()]
		print(uniRank)
	if msg.find('sop') != -1:
		sop = re.findall("\d+\.\d+", msg)
		sop = [float(i) for i in sop]
		print(sop)
	if msg.find('lor') != -1:
		lor = re.findall("\d+\.\d+", msg)
		lor = [float(i) for i in lor]
		print(lor)
	if msg.find('research') != -1 :
		if msg.find('yes')!= -1:
			research = 1
		else:
			research = 0   
		print(research)
	if msg.find('find') != -1 :
		new_data = [(gre[0],cgpa[0],toefl[0],uniRank[0],research,sop[0],lor[0])]
		new_array = np.asarray(new_data)
		labels=["reject","admit"]
		prediction = model.predict(new_array)
		print(prediction)
		if int(prediction) == 1:
			print("Yes. You have a good chance at getting into it.")
		else:
			print("No. You should target a better score or a lower university.")
	if msg.find('bye') != -1 :
		print('Bot> ' + bot.reply('localuser',msg))
		break

	print('Bot> ' + bot.reply('localuser',msg))
    
    
 
