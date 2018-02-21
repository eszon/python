

class PostProcessed(object):

    def __init__(self):
        self.param1 = 'null'

    def fslice(self, param1):
        s = param1.split(' ')[1]
        exec(s + f'{()}')

