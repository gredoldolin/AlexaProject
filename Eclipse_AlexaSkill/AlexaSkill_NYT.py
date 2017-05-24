'''
Created on 06.05.2017

@author: phil
'''

# open ngrok command line and type
# C:\Users\phili\eclipse\workspace\BigData_Project\Alexa>ngrok http 5000
# copy https part and add "/nyt_reader" to it in https://developer.amazon.com/edw/home.html#/skill/amzn1.ask.skill.a58fe0ab-0270-46b2-ae34-b5fcf1b55205/en_US/configuration


from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
#import unidecode

app = Flask(__name__)
ask = Ask(app, "/nyt_reader")

def get_headlines():

    sess = requests.Session()

    url = "http://api.nytimes.com/svc/topstories/v2/home.json?api-key=3b9ad549cdbe4d2b9e8d14a03d67ef3e"
    html = sess.get(url)

    data = json.loads(html.content.decode('utf-8'))
 
    titles = []
    result = data['results']
    
    for listing in result:
        titles.append( listing['title'] )
    return titles  

    
x = get_headlines()
print(x)


@app.route('/')
def homepage():
    return "welcome Sir!"

@ask.launch
def start_skill():
    welcome_message = 'Welcome sir. You look so beautiful today. Would you like the recent top news from the New York Times?'
    return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    headlines = get_headlines()
    headline_msg = 'Alright Sir, I am so glad to announce you the following top headlines {}'.format(headlines)
    return statement(headline_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Why the hell did you asked me than?'
    return statement(bye_text)
    
if __name__ == '__main__':
    app.run(debug=True)
    


