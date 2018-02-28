
class Square(object):
    def __init__(self):
        self.size_side = 2

    def change_side(self, param1):
        self.size_side = param1

    def show_side(self):
        print(f'Side: {self.size_side}')

    def calc_area(self):
        print(f'Area of the square is {self.size_side * self.size_side}')

