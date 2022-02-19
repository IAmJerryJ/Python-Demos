# Runde Jia
# Sydeney
# 2021/11/20 23:00
s='天涯若此时'
print(s.encode(encoding='UTF-8'))
print(s.encode(encoding='GBK'))

byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))

byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))