# Runde Jia
# Sydeney
# 2021/11/23 19:26
print(dir(object))


class A:
    pass


class B:
    pass


class C(B,A):
    def __init__(self,name,age):
        self.name=name
        self.age=age


class D(A):
    pass


x=C('Jack',20)
print(x.__dict__)
print(C.__dict__)
print('------------------')
print(type(x))
print(x.__class__)
print(C.__bases__)   # Tuple
print(C.__base__)
print(C.__mro__)
print(A.__subclasses__())   # List

