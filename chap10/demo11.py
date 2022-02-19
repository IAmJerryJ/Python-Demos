# Runde Jia
# Sydeney
# 2021/11/21 17:12

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


for i in range(1,7):
    print(fib(i))
