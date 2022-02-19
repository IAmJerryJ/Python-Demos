# Runde Jia
# Sydeney
# 2021/11/11 20:19
a,b=10,20
print('a>b? ',a>b)
print('a<b?',a<b)
print('a<=b?',a<=b)
print('a>=b?',a>=b)
print('a==b?',a==b)
print('a!=b?',a!=b)

'''=,  ==
    comparing value not identifier,
    comparing identifier using is
'''
a=10
b=10
print(a==b)  # comparing value
print(a is b)  # comparing identifier

lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)
print(lst1 is lst2)
print(id(lst1),id(lst2))
print(a is not b)
print(lst1 is not b)

