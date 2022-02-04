from flask import Flask, render_template, request
import numpy as np 
from rivescript import RiveScript
import os.path
import pickle

app = Flask(__name__, template_folder="templates")

pkl_filename = "model/pickle_model.pkl"
with open(pkl_filename, 'rb') as file:
	model = pickle.load(file)

file = os.path.dirname("__file__")
convo = os.path.join(file , 'convo')

bot = RiveScript()
bot.load_directory(convo)
bot.sort_replies()

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
	userText = request.args.get('msg')
	msg = userText
	botText=bot.reply('localuser',msg)
	return str(botText)

if __name__ == "__main__":
    app.run()