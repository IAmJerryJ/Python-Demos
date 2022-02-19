# Runde Jia
# Sydeney
# 2021/11/23 19:55

class Person(object):

    def __new__(cls, *args, **kwargs):
        print('__new__ has been used, cls id: {0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('Created object id: {0}'.format(id(obj)))
        return obj

    def __init__(self,name,age):
        print('__init__ has been used, self id: {0}'.format(id(self)))
        self.name=name
        self.age=age


print('object id: {0}'.format(id(object)))
print('Person id: {0}'.format(id(Person)))

p1=Person('Zhangsan',20)
print('p1 id:{0}'.format(id(p1)))
