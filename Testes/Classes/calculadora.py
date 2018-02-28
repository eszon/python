class Calculadora(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subtrai(self):
        return self.a - self.b

    def divisao(self):
        return self.a / self.b

class Calculadora02(object):

    def soma(self, a, b):
        return a + b

    def subtrai(self, a, b):
        return a - b

