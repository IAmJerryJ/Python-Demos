# Runde Jia
# Sydeney
# 2021/11/13 21:13
lst=[10,20,30,40,50,60,70,80]

print('original',id(lst))

lst2=lst[1:6:1]
print('current',id(lst2))
print(lst[1:6])
print(lst[1:6:])
print(lst[1:6:2])
print(lst[:6:2])
print(lst[1::2])
print('----------------------Step is negative----------------------------')
print(lst[::-1])
print(lst[6:1:-1])
