#### Team members:
Christian Kregelin | Philipp Krank | Pranav Pandya
--- | --- | --- | 

## Introduction

This is a project for our course "Enterprise Architecture for Big Data". Alexa is a Amazon's cloud-based “intelligent personal assistant” which processes your requests and supplies answers back through the Echo device. Alexa is was intorduced to the German market fairly recently (Sept '16). It provides great potential for developers to come up with use cases. Our mission is to make use of natural language processing (NLP) in order to build a custom news extraction skill. 

## Project objectives:
* Build an Alexa skill that extracts news from a newspaper according to the user’s interest.
---
This includes:
  * Use Natural Language Processing (NLP)
  * Use Web API for news extraction
  * Delivery of news through voice commands within an 8 secs time limit according to news source, category, mood (sentiment analysis)

## Technologies used:
  * Amazon Echo
  * AWS Cloud
  * Python
  * Eclipse (IDE)
  * Web API
  * Github
  * Flask
  * ngrok

![alt text](https://github.com/pranavpandya84/AlexaProject/blob/master/uploads/01%20how%20echo%20works.PNG)
* The natural language understanding part starts with voice command sent from the user to Amazon echo. Under the hood, voice/speech is converted to text and this is where natural language processing part starts. The output is TTS (Text to Speech) based on logic defined in interaction model. 

![alt text](https://github.com/pranavpandya84/AlexaProject/blob/master/uploads/02%20architecture.PNG)
Note: Audio responses are rendered on device

* For testing our script on our own Amazon Echo device, we used "ngrok", which securely tunnels to our localhost (= our computer or rather the virtual IP-address of the currently running server on our computer).

![alt text](https://github.com/pranavpandya84/AlexaProject/blob/master/uploads/03%20interaction%20model.PNG)
