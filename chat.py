
from rivescript import RiveScript
import os.path

file = os.path.dirname("__file__")
convo = os.path.join(file , 'convo')

bot = RiveScript()
bot.load_directory(convo)
bot.sort_replies()

while True:
    msg = str(input ('You> '))
    #print(msg)
    if msg.find('gre') != -1 :
        gre = [int(i) for i in msg.split() if i.isdigit()] 
        print (gre[0])
        
    if msg.find('cgpa') != -1 :
        cgpa = [int(i) for i in msg.split() if i.isdigit()] 
        print (cgpa[0])
        
    
    print('Bot> ' +bot.reply('localuser',msg))
    
    if msg == 'bye':
        break

