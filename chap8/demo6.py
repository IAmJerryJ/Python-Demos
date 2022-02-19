# Runde Jia
# Sydeney
# 2021/11/18 22:14
s={10,20,30,405,60}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)

s.add(80)
print(s)
s.update({200,400,300})
print(s)
s.update([100,99,8])
s.update((78,64,56))
print(s)

s.remove(100)
print(s)

# s.remove(500)
# print(s)

s.discard(500)
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
# s.pop(400)
s.clear()
print(s)
