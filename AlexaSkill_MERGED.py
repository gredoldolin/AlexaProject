" "'''
Created between 06.05.2017 and 16.07.2017

@authors: phil, ck12, Delta4s2Cyclone
'''

from flask import Flask
from flask_ask import Ask, statement, question, session
from afinn import Afinn
import json
import requests
import operator
#import unidecode

app = Flask(__name__)
ask = Ask(app, "/worldnews")

# Sentiment Analysis with AFINN
afinn = Afinn()


# NYT functions
def get_headlinesHome():
    sess = requests.Session()
    url = "http://api.nytimes.com/svc/topstories/v2/home.json?api-key=3b9ad549cdbe4d2b9e8d14a03d67ef3e"
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = []
    result = data['results']
    
    # announce new headline (e.g. "second headline:")
    counter = 2
    for listing in result:
        titles.append( listing['title'] )
        if counter == 2:
            counter2 = "second"
        elif counter == 3:
            counter2 = "third"
        elif counter == 4:
            counter2 = "fourth"
        elif counter == 5:
            counter2 = "fifth"
        else:
            counter2 = ""
                    
        titles.append( str(counter2) + " headline ..." ) 
        counter = counter + 1 
        
    output = str(titles[:9]) + "... That's all for today. I hope you are now well informed. Have a great day ... Goodbye."
    return output


def get_headlinesSports():
    sess = requests.Session()
    url = "http://api.nytimes.com/svc/topstories/v2/sports.json?api-key=3b9ad549cdbe4d2b9e8d14a03d67ef3e"
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = []
    result = data['results']
    
    # announce new headline (e.g. "second headline:")
    counter = 2
    for listing in result:
        titles.append( listing['title'] )
        if counter == 2:
            counter2 = "second"
        elif counter == 3:
            counter2 = "third"
        elif counter == 4:
            counter2 = "fourth"
        elif counter == 5:
            counter2 = "fifth"
        else:
            counter2 = ""
                    
        titles.append( str(counter2) + " headline ..." ) 
        counter = counter + 1 
    output = str(titles[:9]) + "... That's all for today. I hope you are now well informed. Have a great day ... Goodbye."
    return output


def get_headlinesPolitics():
    sess = requests.Session()
    url = "http://api.nytimes.com/svc/topstories/v2/politics.json?api-key=3b9ad549cdbe4d2b9e8d14a03d67ef3e"
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = []
    result = data['results']
    
    # announce new headline (e.g. "second headline:")
    counter = 2
    for listing in result:
        titles.append( listing['title'] )
        if counter == 2:
            counter2 = "second"
        elif counter == 3:
            counter2 = "third"
        elif counter == 4:
            counter2 = "fourth"
        elif counter == 5:
            counter2 = "fifth"
        else:
            counter2 = ""
                    
        titles.append( str(counter2) + " headline ..." ) 
        counter = counter + 1 
    output = str(titles[:9]) + "... That's all for today. I hope you are now well informed. Have a great day ... Goodbye."
    return output


def get_headlinesTechnology():
    sess = requests.Session()
    url = "http://api.nytimes.com/svc/topstories/v2/technology.json?api-key=3b9ad549cdbe4d2b9e8d14a03d67ef3e"
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = []
    result = data['results']
    
    # announce new headline (e.g. "second headline:")
    counter = 2
    for listing in result:
        titles.append( listing['title'] )
        if counter == 2:
            counter2 = "second"
        elif counter == 3:
            counter2 = "third"
        elif counter == 4:
            counter2 = "fourth"
        elif counter == 5:
            counter2 = "fifth"
        else:
            counter2 = ""
                    
        titles.append( str(counter2) + " headline ..." ) 
        counter = counter + 1 
    output = str(titles[:9]) + "... That's all for today. I hope you are now well informed. Have a great day ... Goodbye."
    return output


# TOI functions
def get_headlinesTop():
    sess = requests.Session()
    url = "https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=3534992ea6b64a28866c01fcc2cfba24"
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = []
    result = data['articles']
    
    # announce new headline (e.g. "second headline:")
    counter = 2
    for listing in result:
        titles.append( listing['title'] )
        if counter == 2:
            counter2 = "second"
        elif counter == 3:
            counter2 = "third"
        elif counter == 4:
            counter2 = "fourth"
        elif counter == 5:
            counter2 = "fifth"
        else:
            counter2 = ""
                    
        titles.append( str(counter2) + " headline ..." ) 
        counter = counter + 1 
    output = str(titles[:9]) + "... That's all for today. I hope you are now well informed. Have a great day ... Goodbye."
    return output

def get_headlinesLatest():
    sess = requests.Session()
    url = "https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=latest&apiKey=3534992ea6b64a28866c01fcc2cfba24"
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = []
    result = data['articles']
    
    # announce new headline (e.g. "second headline:")
    counter = 2
    for listing in result:
        titles.append( listing['title'] )
        if counter == 2:
            counter2 = "second"
        elif counter == 3:
            counter2 = "third"
        elif counter == 4:
            counter2 = "fourth"
        elif counter == 5:
            counter2 = "fifth"
        else:
            counter2 = ""
                    
        titles.append( str(counter2) + " headline ..." ) 
        counter = counter + 1    
    output = str(titles[:9]) + "... That's all for today. I hope you are now well informed. Have a great day ... Goodbye."
    return output


# Sentiment NYT
def get_negativeSentimentNYT():
    sess = requests.Session()
    url = "http://api.nytimes.com/svc/topstories/v2/home.json?api-key=3b9ad549cdbe4d2b9e8d14a03d67ef3e"
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = []
    result = data['results']
    
    for listing in result:
        titles.append( listing['title'] )
    
    # Sentiment score for each headline.
    afinn_scores = [afinn.score(text) for text in titles]
    headline_sentiment = dict(zip(titles, afinn_scores))
    sorted_x = dict(sorted(headline_sentiment.items(), key=operator.itemgetter(1)))
    
    # Get rid of the score values, so that Alexa doesn't read it out.
    ergebnis = []
 
     # announce new headline (e.g. "second headline:")
    counter = 2
       
    for k, v in sorted_x.items():
        ergebnis.append(k)
        if counter == 2:
            counter2 = "second"
        elif counter == 3:
            counter2 = "third"
        #elif counter == 4:
        #    counter2 = "fourth"
        #elif counter == 5:
        #    counter2 = "fifth"
        else:
            counter2 = ""
                     
        ergebnis.append( str(counter2) + " most awful headline ..." ) 
        counter = counter + 1        
    
    output = str(ergebnis[:5]) + "... That's all for today. What a sick world we are living in ... Anyway ... I wish you a great day. Goodbye."
    return output



def get_positiveSentimentNYT():
    sess = requests.Session()
    url = "http://api.nytimes.com/svc/topstories/v2/home.json?api-key=3b9ad549cdbe4d2b9e8d14a03d67ef3e"
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = []
    result = data['results']
    
    for listing in result:
        titles.append( listing['title'] )
    
    # Sentiment score for each headline.
    afinn_scores = [afinn.score(text) for text in titles]
    headline_sentiment = dict(zip(titles, afinn_scores))
    sorted_x = dict(sorted(headline_sentiment.items(), key=operator.itemgetter(1), reverse=True))

    # Get rid of the score values, so that Alexa doesn't read it out.
    ergebnis = []
    
     # announce new headline (e.g. "second headline:")
    counter = 2
       
    for k, v in sorted_x.items():
        ergebnis.append(k)
        if counter == 2:
            counter2 = "second"
        elif counter == 3:
            counter2 = "third"
        #elif counter == 4:
        #    counter2 = "fourth"
        #elif counter == 5:
        #    counter2 = "fifth"
        else:
            counter2 = ""
                     
        ergebnis.append( str(counter2) + " happiest headline ..." ) 
        counter = counter + 1        
        
    output = str(ergebnis[:5]) + "... That's all for today. Yippie Yippie Yeah ... happy news everywhere. I wish you a great day. Goodbye."
    return output


# Sentiment TOI
def get_negativeSentimentTOI():
    sess = requests.Session()
    url = "https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=latest&apiKey=3534992ea6b64a28866c01fcc2cfba24"
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = []
    result = data['articles']
    
    for listing in result:
        titles.append( listing['title'] )
        titles = [w.replace(' - Times of India', '') for w in titles]

    # Sentiment score for each headline.    
    afinn_scores = [afinn.score(text) for text in titles]
    headline_sentiment = dict(zip(titles, afinn_scores))
    sorted_x = dict(sorted(headline_sentiment.items(), key=operator.itemgetter(1)))
    
    # Get rid of the score values, so that Alexa doesn't read it out.
    ergebnis = []
     # announce new headline (e.g. "second headline:")
    counter = 2
       
    for k, v in sorted_x.items():
        ergebnis.append(k)
        if counter == 2:
            counter2 = "second"
        elif counter == 3:
            counter2 = "third"
        #elif counter == 4:
        #    counter2 = "fourth"
        #elif counter == 5:
        #    counter2 = "fifth"
        else:
            counter2 = ""
                     
        ergebnis.append( str(counter2) + " most horrible headline ..." ) 
        counter = counter + 1        
        
    output = str(ergebnis[:5]) + "... That's all for today. What a sick world we are living in ... Anyway ... I wish you a great day. Goodbye."
    return output   


def get_positiveSentimentTOI():
    sess = requests.Session()
    url = "https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=latest&apiKey=3534992ea6b64a28866c01fcc2cfba24"
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = []
    result = data['articles']
    
    for listing in result:
        titles.append( listing['title'] )
        titles = [w.replace(' - Times of India', '') for w in titles]
    
    # Sentiment score for each headline.
    afinn_scores = [afinn.score(text) for text in titles]
    headline_sentiment = dict(zip(titles, afinn_scores))
    sorted_x = dict(sorted(headline_sentiment.items(), key=operator.itemgetter(1), reverse=True))

    # Get rid of the score values, so that Alexa doesn't read it out.
    ergebnis = []
     # announce new headline (e.g. "second headline:")
    counter = 2
       
    for k, v in sorted_x.items():
        ergebnis.append(k)
        if counter == 2:
            counter2 = "second"
        elif counter == 3:
            counter2 = "third"
        #elif counter == 4:
        #    counter2 = "fourth"
        #elif counter == 5:
        #    counter2 = "fifth"
        else:
            counter2 = ""
                     
        ergebnis.append( str(counter2) + " most joyful headline ..." ) 
        counter = counter + 1        
        
    output = str(ergebnis[:5]) + "... That's all for today. Yippie Yippie Yeah ... joyful news everywhere. I wish you a great day. Goodbye."
    return output



## Welcome message.
@app.route('/')
def homepage():
    return "Welcome Sir!"


## Launch the skill in Alexa.
@ask.launch
def start_skill():
    welcome_message = "Welcome Professor Mueller ... you smart Business Intelligence students ... and our extremely good looking guests ... Which news source would you like to hear? We've got the New York Times or the Times of India exclusively for you."
    return question(welcome_message)


## Initiate source.
@ask.intent("YesIntentNYT")
def start_NYT():
    welcome_NYT = "New York ... concrete jungle where dreams are made of. Would you like to hear the happiest articles ... or the most awful ones. You can also choose news from your favorite category ... Most popular News...Sports...Technology...or Politics."
    return question(welcome_NYT)

@ask.intent("YesIntentTOI")
def start_TOI():
    welcome_TOI = "India ... homeland of gorgeous Pranaph. Would you like to hear the most joyful articles ... or the most horrible ones. You can also choose between the top news ... and the latest news."    
    return question(welcome_TOI)


## NYT source
@ask.intent("YesIntentHome")
def share_headlines():
    headlines = get_headlinesHome()
    headline_msg = 'Alright Sir, I am so glad to announce you the following most popular headlines {}'.format(headlines)
    return statement(headline_msg)

@ask.intent("YesIntentSports")
def share_headlines():
    headlines = get_headlinesSports()
    headline_msg = 'Alright Sir, I am so glad to announce you the following top headlines for sports {}'.format(headlines)
    return statement(headline_msg)

@ask.intent("YesIntentPolitics")
def share_headlines():
    headlines = get_headlinesPolitics()
    headline_msg = 'Alright Sir, I am so glad to announce you the following top headlines for politics {}'.format(headlines)
    return statement(headline_msg)

@ask.intent("YesIntentTechnology")
def share_headlines():
    headlines = get_headlinesTechnology()
    headline_msg = 'Alright Sir, I am so glad to announce you the following top headlines for technology{}'.format(headlines)
    return statement(headline_msg)


## TOI source.
@ask.intent("YesIntentTop")
def share_headlines():
    headlines = get_headlinesTop()
    headline_msg = 'Alright Sir, I am so glad to announce you the following top headlines {}'.format(headlines)
    return statement(headline_msg)

@ask.intent("YesIntentLatest")
def share_headlines():
    headlines = get_headlinesLatest()
    headline_msg = 'Alright Sir, I am so glad to announce you the following latest headlines {}'.format(headlines)
    return statement(headline_msg)

## NYT sentiment
@ask.intent("YesIntentNYTSentimentPositive")
def share_headlines():
        headlines = get_positiveSentimentNYT()
        headline_msg = 'Alright Sir, I am so glad to announce you the following three happiest headlines {}'.format(headlines)
        return statement(headline_msg)

@ask.intent("YesIntentNYTSentimentNegative")
def share_headlines():
        headlines = get_negativeSentimentNYT()
        headline_msg = 'Alright Sir, I am so sad to announce you the following top three most awful articles {}'.format(headlines)
        return statement(headline_msg)


## TOI sentiment
@ask.intent("YesIntentTOISentimentPositive")
def share_headlines():
        headlines = get_positiveSentimentTOI()
        headline_msg = 'Alright Sir, I am so glad to announce you the following three most joyful headlines {}'.format(headlines)
        return statement(headline_msg)

@ask.intent("YesIntentTOISentimentNegative")
def share_headlines():
        headlines = get_negativeSentimentTOI()
        headline_msg = 'Alright Sir, I am so sad to announce you the following top three most horrible articles {}'.format(headlines)
        return statement(headline_msg)

## No intent
@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Why the hell did you asked me than?'
    return statement(bye_text)

## Print results

b = get_negativeSentimentNYT()
print(b)

bb = get_positiveSentimentNYT()
print(bb)

bbb = get_negativeSentimentTOI()
print(bbb)

bbbb = get_positiveSentimentTOI()
print(bbbb)


# TOI
#x = get_headlinesTop()
#print(x)
#y = get_headlinesLatest()
#print(y)
    
# NYT
#x = get_headlinesHome()
#print(x)   
#y = get_headlinesSports()
#print(y)    
#z = get_headlinesTechnology()
#print(z)    
#aa = get_headlinesPolitics()
#print(aa)
    
if __name__ == '__main__':
    app.run(debug=True)