# Runde Jia
# Sydeney
# 2021/11/13 21:35
lst=[10,20,30]
print('before',lst,id(lst))
lst.append(100)
print('after',lst,id(lst))
lst2=['hello','world']
lst.append(lst2)
print(lst)
lst.extend(lst2)
print(lst)
lst.insert(1,90)
print(lst)

lst3=[True,False,'hello']
lst[1:3]=lst3
print(lst)
