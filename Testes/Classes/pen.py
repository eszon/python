
class Pen(object):
    def __init__(self):
        self.model = 'BAND'


    @property
    def getModel(self):
        return self.__model

    @getModel.setter
    def getModel(self, m):
        self.__getModel = m
        print(self.__getModel)





