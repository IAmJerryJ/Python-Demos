# Runde Jia
# Sydeney
# 2021/11/21 17:24
try:
    a=int(input('Enter first number'))
    b=int(input('Enter second number'))

    result=a/b
    print('The result is:',result)
except ZeroDivisionError:
    print('divider cannot be zero')
print('Program ends')
