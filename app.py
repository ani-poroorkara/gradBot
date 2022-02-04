from flask import Flask, render_template, request
import re
import numpy as np 
from rivescript import RiveScript
import os.path
import pickle

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():

	pkl_filename = "model/pickle_model.pkl"
	with open(pkl_filename, 'rb') as file:
		model = pickle.load(file)

	file = os.path.dirname("__file__")
	convo = os.path.join(file , 'convo')
	
	bot = RiveScript()
	bot.load_directory(convo)
	bot.sort_replies()
	while True:
		userText = request.args.get('msg')
		msg = userText

		if msg.find('gre') != -1 :
			global gre
			gre = [int(i) for i in msg.split() if i.isdigit()] 

		if msg.find('cgpa') != -1 :
			global cgpa
			cgpa = re.findall("\d+\.\d+", msg)
			cgpa = [float(i) for i in cgpa]
			
		if msg.find('toefl') != -1 :
			global toefl
			toefl = [int(i) for i in msg.split() if i.isdigit()] 
			
		if msg.find('rank') != -1 :
			global uniRank
			uniRank = [int(i) for i in msg.split() if i.isdigit()] 
			
		if msg.find('sop') != -1 :
			global sop
			sop = re.findall("\d+\.\d+", msg)
			sop = [float(i) for i in sop] 
			
		if msg.find('lor') != -1 :
			global lor
			lor = re.findall("\d+\.\d+", msg)
			lor = [float(i) for i in lor]
			
		if msg.find('research') != -1 :
			global research
			if msg.find('yes')!= -1:
				research = 1
			else:
				research = 0
		
		if msg.find('find') != -1 :
			new_data = [(gre[0],cgpa[0],toefl[0],uniRank[0],research,sop[0],lor[0])]
			new_array = np.asarray(new_data)
			labels=["reject","admit"]
			prediction=model.predict(new_array)
			botText= labels[int(prediction) ]+'. Do you want to start again?'
			return str(botText)

		if msg == 'bye':
			break

		botText=bot.reply('localuser',msg)
		return str(botText)
		
if __name__ == "__main__":
    app.run(debug=False)