# Runde Jia
# Sydeney
# 2021/11/21 17:33
try:
    a=int(input('Enter first number'))
    b=int(input('Enter second number'))
    result=a/b
except BaseException as e:
    print('Error!',e)
else:
    print('The resutl is: ',result)