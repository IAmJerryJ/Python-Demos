# Runde Jia
# Sydeney
# 2021/11/14 19:17
items=['Fruits','Books','Others']
prices=[96,78,85]

d={item.upper():price for item,price in zip(items, prices)}
print(d)
