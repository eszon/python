from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot, chatterbot
import os
from datetime import datetime
from class_preprocess import PreProcessed

#log = logging.basicConfig(level=logging.INFO)
cpp = PreProcessed()
chatbot = ChatBot("Mia") # Name of bot
chatbot.set_trainer(ListTrainer)

path = "C:/Users/igor.vieira/Documents/Documentos/Github/python/Testes/Chat/Chatbot/knowledge/"
dir = os.listdir(path)

for file in os.listdir(path):
    chats = open(path + file, mode='r', encoding='utf-8').readlines()
    #chatbot.train(chats)

while True:
    try:
     request = input(f'{cpp.ftime()} You: ', )

     response = chatbot.get_response(request)
     response1 = response.text

     cpp.logicfuc(response1)

     #print(f'{fhour()} Mia: ', response, )

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

