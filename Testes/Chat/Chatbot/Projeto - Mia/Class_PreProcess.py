from datetime import datetime

class PreProcessed(object):

    def ftime(self):
        now = datetime.now()
        print(f'{now.hour}:{now.minute}:{now.second} ', end='')
        ##{now.day} / {now.month} / {now.year}

    def fslice(self, param1):
        s = param1.split(' ')[1]
        print(s)
        exec(f'self.{s}' + f'{()}')


    def logicfuc(self, param2):
        #cpp = PreProcessed
        response2 = param2.split(' ')[0]
        if response2 == 'function':
            print('9Mia:', end=' ')
            self.fslice(param2)

        else:
           print(f'{self.ftime()} Mia: ', param2, )

    def helloworld(self):
        print('Fucking Hello World!')




