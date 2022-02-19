# Runde Jia
# Sydeney
# 2021/11/12 14:31
money=1000
s=int(input('Enter withdraw amount'))
#   Determine balance is sufficient or not
if money>=s:
    money=money-s
    print('Withdraw successful, balance is: ', money)
