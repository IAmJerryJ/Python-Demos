# Runde Jia
# Sydeney
# 2021/11/12 22:25
num_a=int(input('Please enter first integer'))
num_b=int(input('Please enter second integer'))

'''if num_a>num_b:
    print(num_a,'>=',num_b)
else:
    print(num_a,'<',num_b)
'''
print(str(num_a)+'>='+str(num_b) if num_a>=num_b else str(num_a)+'<'+str(num_b))
