
class Pen(object):
    def __init__(self):
        self.model = 'BAND'



    def getModel01(self):
        print(f'Public Method: {self.model}')


    def __getModel02(self, m):
        print(f'Private Method: {self.model}')






