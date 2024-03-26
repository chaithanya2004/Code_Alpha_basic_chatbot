import random
import nltk
from nltk.chat.util import Chat, reflections
Conversation=[
    ('hi|hello|hey there',['Hello!','Hey!','Hi there!']),
    ('what is your name?',['I am a TechRobo']),
    ('Are you intelligent meshin?',['yes']),
    ('how old are you?',['I don\'t have an age.I am a TechRobo']),
    ('what is the weather like today?',['I am sorry,I cannot provide real-time weather information.']),
    ('do you provide information about the world?',['yes,I can.']),
    ('Tell about genaral knowledge about world',['Sure! Here are the some genaral knowledge concepts of world ']),
    ('Thank you',['Your always welcome']),
    ('bye',['Goodbye! have a nice day!']),
    ('exit',[':)']),
    ('.*',['I am sorry, I didn\'t understand that.']),
]
genaral_knowledge=(" 8 wonders of world :\n1) Greate wall of china\n2) Chichen Itza in Jordan\n3)Petra in Brazil\n4)Machh Picchu in Peru\n5)chirst the Redeemer in Brazil\n6)colossem in Italy\n7)Taj Mahal\n8)Angkor Wat in Cambodia") 
chatbot=Chat(Conversation, reflections)
print("Welcome!Now lets talk: How can I help you?")
while True:
    user_input=input("User: ")
    if 'About world' in user_input:
       print("Chatbot:")
       print(genaral_knowledge)
    else:
       response=chatbot.respond(user_input)
       print("Chatbot:",response)
    if __name__=="__main__":
        if(user_input=="exit"):
         print("Thank you for using TechRobo")
