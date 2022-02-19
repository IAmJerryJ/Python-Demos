# Runde Jia
# Sydeney
# 2021/11/13 22:10
lst=[20,40,10,98,54]
print('Before sorting',lst,id(lst))
lst.sort()
print('After sorting',lst,id(lst))
lst.sort(reverse=True)
print(lst)
lst.sort(reverse=False)
print(lst)

print('------------sorted------------')
lst=[20,40,10,98,54]
print('Original',lst)
new_list=sorted(lst)
print(lst,id(lst))
print(new_list,id(new_list))
desc_list=sorted(lst,reverse=True)
print(desc_list)
