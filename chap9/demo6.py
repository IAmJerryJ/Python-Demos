# Runde Jia
# Sydeney
# 2021/11/19 22:05

s='hello world python'
lst=s.split()
print(lst)

s1='hello|world|Python'
print(s1.split())
print(s1.split(sep='|'))
print(s1.split(sep='|',maxsplit=1))

print(s.rsplit())
print(s.rsplit(maxsplit=1))
