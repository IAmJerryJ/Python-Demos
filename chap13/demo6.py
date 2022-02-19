# Runde Jia
# Sydeney
# 2021/11/23 18:59
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return 'My name is {0}, age is {1}'.format(self.name,self.age)


stu=Student('Zhangsan',20)
print(dir(stu))
print(stu)
print(type(stu))