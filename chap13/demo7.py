# Runde Jia
# Sydeney
# 2021/11/23 19:10
class Animal(object):
    def eat(self):
        print('Animal eats staff')


class Dog (Animal):
    def eat(self):
        print('Dog eats bones')


class Cat(Animal):
    def eat(self):
        print('Cat eats fish')


class Person:
    def eat(self):
        print('People eats meal')


def fun(obj):
    obj.eat()


fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())