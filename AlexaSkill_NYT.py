'''
Created on 06.05.2017

@author: phil
'''

from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
#import unidecode

app = Flask(__name__)
ask = Ask(app, "/nyt_reader")



def get_headlinesHome():

    sess = requests.Session()

    url = "http://api.nytimes.com/svc/topstories/v2/home.json?api-key=3b9ad549cdbe4d2b9e8d14a03d67ef3e"
    html = sess.get(url)

    data = json.loads(html.content.decode('utf-8'))
 
    titles = []
    result = data['results']
    
    for listing in result:
        titles.append( listing['title'] )
    return titles  



def get_headlinesSports():

    sess = requests.Session()

    url = "http://api.nytimes.com/svc/topstories/v2/sports.json?api-key=3b9ad549cdbe4d2b9e8d14a03d67ef3e"
    html = sess.get(url)

    data = json.loads(html.content.decode('utf-8'))
 
    titles = []
    result = data['results']
    
    for listing in result:
        titles.append( listing['title'] )
    return titles  



def get_headlinesPolitics():

    sess = requests.Session()

    url = "http://api.nytimes.com/svc/topstories/v2/politics.json?api-key=3b9ad549cdbe4d2b9e8d14a03d67ef3e"
    html = sess.get(url)

    data = json.loads(html.content.decode('utf-8'))
 
    titles = []
    result = data['results']
    
    for listing in result:
        titles.append( listing['title'] )
    return titles  



def get_headlinesTechnology():

    sess = requests.Session()

    url = "http://api.nytimes.com/svc/topstories/v2/technology.json?api-key=3b9ad549cdbe4d2b9e8d14a03d67ef3e"
    html = sess.get(url)

    data = json.loads(html.content.decode('utf-8'))
 
    titles = []
    result = data['results']
    
    for listing in result:
        titles.append( listing['title'] )
    return titles  


    
x = get_headlinesHome()
print(x)    
y = get_headlinesSports()
print(y)    
z = get_headlinesTechnology()
print(z)    
aa = get_headlinesPolitics()
print(aa)


@app.route('/')
def homepage():
    return "welcome Sir!"

@ask.launch
def start_skill():
    welcome_message = 'Welcome sir. You look so beautiful today. Which recent news do you like to hear from the New York Times? We have the following categories available... Top News...Sports...Technology...and Politics'
    return question(welcome_message)


@ask.intent("YesIntentHome")
def share_headlines():
    headlines = get_headlinesHome()
    headline_msg = 'Alright Sir, I am so glad to announce you the following top headlines {}'.format(headlines)
    return statement(headline_msg)


@ask.intent("YesIntentSports")
def share_headlines():
    headlines = get_headlinesSports()
    headline_msg = 'Alright Sir, I am so glad to announce you the following top headlines {}'.format(headlines)
    return statement(headline_msg)


@ask.intent("YesIntentPolitics")
def share_headlines():
    headlines = get_headlinesPolitics()
    headline_msg = 'Alright Sir, I am so glad to announce you the following top headlines {}'.format(headlines)
    return statement(headline_msg)


@ask.intent("YesIntentTechnology")
def share_headlines():
    headlines = get_headlinesTechnology()
    headline_msg = 'Alright Sir, I am so glad to announce you the following top headlines {}'.format(headlines)
    return statement(headline_msg)


@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Why the hell did you asked me than?'
    return statement(bye_text)
    
if __name__ == '__main__':
    app.run(debug=True)