# Runde Jia
# Sydeney
# 2021/11/14 18:55
scores={'Zhangsan':100,'Lisi':98,'Wangwu':45}
print('Zhangsan' in scores)
print('Zhangsan' not in scores)

del scores['Zhangsan']
print(scores)

scores.clear()
print(scores)

scores['Chenliu']=98
print(scores)

scores['Chenliu']=100
print(scores)
