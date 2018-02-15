


class Robot(object):

    def __init__(self):
        self.charge = 20
        print('Construtor chamado com sucesso!')

    def walk(self):
        passos = 0
        while self.charge > 5:
            passos += 1
            print('Walking...')
            print(f'Charge: {self.charge}')
            self.charge -= 10
            if self.charge < 5:
                print(f'Conseguir dar {passos} passos, estou sem bateria...')

    def recharge(self):
        self.charge += 50
        print(f'Recarreguei + 50 de bateria, estou com {self.charge}')








