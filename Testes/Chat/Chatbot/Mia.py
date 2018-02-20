# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
from datetime import datetime


def fhour():
    now = datetime.now()
    print(f'{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}:{now.second}')


chatbot = ChatBot("Mia")
chatbot.set_trainer(ListTrainer)

path = "C:/Users/igor.vieira/Documents/Documentos/Github/python/Testes/Chat/Chatbot/knowledge/"
dir = os.listdir(path)

for file in os.listdir(path):
    chats = open(path + file, mode='r', encoding='utf-8').readlines()
    chatbot.train(chats)

while True:
    try:
     request = input('You: ')

     response = chatbot.get_response(request)
     if response == 'RESPONDE_HORA':
         print('9Mia: ', end=' ')
         fhour()
     else:
        print('Mia: ', response, )


    except(KeyboardInterrupt, EOFError, SystemExit):
        break