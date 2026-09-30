#this is my first AI project
#This is simple AI Chatbot created by using Python language

import datetime
import time

name=input("Welcome, Enter your name:")
presentHour=datetime.datetime.now().hour

if 5<= presentHour<=11:
    print("good Morning,",name)
elif 11<= presentHour <= 17:
    print("Good afternoon,",name)
elif 17 <= presentHour <=  20: 
    print("good evening,",name)
else:
    print("Good night",name)    

print("hi i am smart AI chatbot")
print("Ask me simple question and type 'by' to exit from bot ")

#responses dictionary

responses={
    "hello":"Hi,welcome. How can i help you?",
    "how are you":"I am very fine. Thank you",
    "who are you":"I am smart AI chatbot",
    "motivate me":"Keep going. Every bug of your project makes you a better developer",
    "what is your name":"I dont have any name because i am a AI",
    "hi":"Hello, How can i help you",
    "give your self introduction":"I am smart AI chatbot",
    "by":"ok bye"
}

#method to get response from chatbot

def getResponseOfBot(userInput):
    userInput=userInput.lower()
    for eachKey in responses:
        if eachKey in userInput:
            return responses[eachKey]

    return" I am not able to tell that yet. i am still in learning mode"   

#loop to print chatbot response

while True:
    userInput=input("Please ask your question:")
    reply=getResponseOfBot(userInput)
    print("Bot Response:", reply)
#if user type by then it come out of the code
    if "by" in userInput.lower():
        break


