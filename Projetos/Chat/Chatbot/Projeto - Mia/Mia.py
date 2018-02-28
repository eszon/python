from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot, chatterbot
import os
from class_preprocess import PreProcessed

#log = logging.basicConfig(level=logging.INFO)
cpp = PreProcessed()
chatbot = ChatBot("Mia") # Name of bot
chatbot.set_trainer(ListTrainer)

path = "C:/Users/igor.vieira/Documents/Documentos/Github/python/Projetos/Chat/Chatbot/knowledge/"
dir = os.listdir(path)

for file in os.listdir(path):
    chats = open(path + file, mode='r', encoding='utf-8').readlines()
    #chatbot.train(chats)

while True:
    try:
     request = input(f'{cpp.call_time()} You: ', )

     response = chatbot.get_response(request)

     cpp.call_logic(response.text)



    except(KeyboardInterrupt, EOFError, SystemExit):
        break

