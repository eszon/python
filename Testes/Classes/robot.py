


class robot(object):

    def walk(self):
        print('Walking...')
        robot.charge(self, -21)

    def stop(self):
        print('Stop Walking.')


    def charge(self, a):
        charge = a - 20
        while charge >= 20:
            print(charge)
            if charge == 0:
                print('Não tenho bateria para andar.')


