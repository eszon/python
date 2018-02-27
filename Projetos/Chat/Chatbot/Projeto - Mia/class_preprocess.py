from datetime import datetime

class PreProcessed(object):

    def call_time(self):
        now = datetime.now()
        print(f'{now.hour}:{now.minute}:{now.second} ', end='')
        return 0
        ##{now.day} / {now.month} / {now.year}

    def call_funcexec(self, param1):
        s = param1.split(' ')[1]
        exec(f'self.{s}' + f'{()}')


    def call_logic(self, param2):
        #response2 = param2.split(' ')[0]
        if param2.startswith("function"):   # startswitch verifica se começa com 'string'
        #if response2 == 'function':
            print(f'{self.call_time():} Mia:', end=' ')
            self.call_funcexec(param2)

        else:
           print(f'{self.call_time()} Mia: ', param2, )




#Teste
    def helloworld(self):
        print('Fucking Hello World!')




