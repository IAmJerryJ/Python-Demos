# Runde Jia
# Sydeney
# 2021/11/23 17:26

class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('Engine has started')

car=Car('BMW')
car.start()
print(car.brand)