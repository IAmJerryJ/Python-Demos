# Runde Jia
# Sydeney
# 2021/11/22 15:51
class Student:
    native_place='Hebei'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print('Student is eating')

    @staticmethod
    def method():
        print('I have used staticmethod, I am static method')

    @classmethod
    def cm(cls):
        print('I am class method')


print(Student.native_place)
stu1=Student('Zhangsan',20)
stu2=Student('Lisi',30)
Student.native_place='Tianjin'
print(stu1.native_place)
print(stu2.native_place)
Student.cm()
Student.method()
