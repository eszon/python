# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot, chatterbot
import os
from datetime import datetime


def fhour(): # Return time.
    now = datetime.now()
    print(f'São {now.hour}:{now.minute}:{now.second}.')
    #{now.day} / {now.month} / {now.year}

def fslice(param1):
    s = param1.split(' ')[1]
    print(s + f'{()}')

def helloworld():
    print('Fucking Hello World!')

chatbot = ChatBot("Mia") # Name of bot
chatbot.set_trainer(ListTrainer)

path = "C:/Users/igor.vieira/Documents/Documentos/Github/python/Testes/Chat/Chatbot/knowledge/"
dir = os.listdir(path)

for file in os.listdir(path):
    chats = open(path + file, mode='r', encoding='utf-8').readlines()
    chatbot.train(chats)

while True:
   # try:
     request = input('You: ')

     response = chatbot.get_response(request)

     response2 = response.split(' ')

'''
    if response2 == 'function':
        print('9Mia:', end=' ')
        fslice(response)

     else:
        print('Mia: ', response, )
'''

    #except(KeyboardInterrupt, EOFError, SystemExit):
     #   break