# Runde Jia
# Sydeney
# 2021/11/23 17:34
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
        print(self.name,self.__age)

stu=Student('Zhangsan',20)
stu.show()

print(stu.name)
# print(stu.__age)
print(dir(stu))
print(stu._Student__age)