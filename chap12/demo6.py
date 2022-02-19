# Runde Jia
# Sydeney
# 2021/11/23 17:06
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+' is eating')

stu1=Student('Zhangsan',20)
stu2=Student('Lisi',30)

print(id(stu1))
print(id(stu2))
print('-------------------------')
stu2.gender='Female'
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)

print('------------------------')
stu1.eat()
stu2.eat()

def show():
    print('Function')

stu1.show=show
stu1.show()
