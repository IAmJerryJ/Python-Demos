# Runde Jia
# Sydeney
# 2021/11/21 0:04
def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even


lst = [10,29,34]
print(fun(lst))


def fun1():
    print('hello')


fun1()


def fun2():
    return 'hello'


res=fun2()
print(res)


def fun3():
    return 'hello','world'


print(fun3())