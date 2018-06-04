
class mia():

    def __init__(self):
        self.nome = "Mia"

    def talk(self, param1):
        my_list01 = ['name', 'what', 'is', 'your', 'qual', 'seu', 'nome']
        my_list02 = ['How', 'are', 'you']
        if param1 in my_list01:
            print('Hi, my name is Mia!')

        elif param1 in my_list02:
          print('I am fine and you?')
          


        else:
            print('I do not can talk about this, yet')


