# Runde Jia
# Sydeney
# 2021/11/19 12:32
s='hello.python'
a=s.upper()
print(a,id(a))
print(s,id(s))
print(s.lower(),id(s.lower()))
print(id(s.lower()))
print(s==s.lower())
print(s is (s.lower()))
s2='hello,Python'
print(s2.swapcase())
print(s2.title())
