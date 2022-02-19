# Runde Jia
# Sydeney
# 2021/11/13 0:38

for item in range(100,1000):
    last = item%10
    mid = item//10%10
    first = item//100
    if item==last**3+mid**3+first**3:
        print(item)
