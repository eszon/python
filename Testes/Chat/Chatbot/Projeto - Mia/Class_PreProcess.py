from datetime import datetime

class PreProcessed(object):

    def ftime(self):
        now = datetime.now()
        print(f'{now.hour}:{now.minute}:{now.second} ', end='')
        ##{now.day} / {now.month} / {now.year}

    def fslice(self, param1):
        s = param1.split(' ')[1]
        print(s)
        cpp = PreProcessed()
        exec(cpp + s + f'{()}')


    def logicfuc(self, param2):
        response2 = param2.split(' ')[0]
        if response2 == 'function':
            print('9Mia:', end=' ')
            self.fslice(param2)

        else:
           print(f'{fhour()} Mia: ', param2, )

    def helloworld(self):
        print('Fucking Hello World!')




