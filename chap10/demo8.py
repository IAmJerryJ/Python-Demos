# Runde Jia
# Sydeney
# 2021/11/21 10:54
def fun(a,b=10):
    print('a=',a)
    print('b=',b)

def fun2(*args):
    print(args)

def fun3(**args2):
    print(args2)

fun2(10,20,30,40)
fun3(a=11,b=22,c=33)

def fun4(a,b,*,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)


fun4(10,20,c=30,d=40)


def fun5(a,b,*,c,d,**args):
    pass


def fun6(*args1,**args2):
    pass

def fun7(a,b=10,*args,**args2):
    pass