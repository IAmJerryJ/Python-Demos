# Runde Jia
# Sydeney
# 2021/11/23 19:36
a = 20
b = 100
c=a+b
d=a.__add__(b)
print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name=name

    def __add__(self, other):
        return self.name+other.name

    def __len__(self):
        return len(self.name)


stu1=Student('Zhangsan')
stu2=Student('Lisi')
s=stu1+stu2
print(s)

s=stu1.__add__(stu2)
print(s)
print('------------------')
lst=[11,22,33,44]
print(len(lst))
print(lst.__len__())
print(len(stu1))