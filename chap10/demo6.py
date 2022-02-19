# Runde Jia
# Sydeney
# 2021/11/21 10:30
def fun(*args):
    print(args)
    print(args[0])


fun(10)
fun(10,30)


def fun1(**args):
    print(args)


fun1(a=10)
fun1(a=20,b=30,c=40)


'''def fun2(*args, *a):
    pass'''

'''def fun2(**args, **arg1s):
    pass'''


def fun2(*args1,**args2):
    pass


'''def fun3(**args1, *args2):
    pass'''

