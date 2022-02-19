# Runde Jia
# Sydeney
# 2021/11/13 21:48
lst=[10,20,30,40,50,60,30]
lst.remove(30)
print(lst)
# lst.remove(100)
lst.pop(1)
print(lst)
# lst.pop(5)
lst.pop()
print(lst)
print('-------------------------')
new_lst=lst[1:3]
print('original',lst)
print('new',new_lst)
print(id(lst))
print(id(lst[1:3]))
i=1
b=i
print(id(i),id(b))
lst[1:3]=[]
print(lst)

lst.clear()
print(lst)
del lst
# print(lst)

