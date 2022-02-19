# Runde Jia
# Sydeney
# 2021/11/12 14:55
answer=input('Are you a member?y/n')
money=float(input('Please enter your shopping amount'))

if answer=='y' :
    if money>=200:
        print('Pay amount is:', money*0.8)
    elif money >= 100:
        print('Pay amount is:',money*0.9)
    else:
        print('Pay amount is:', money)
else:
    if money>=200:
        print('Pay amount is:', money*0.95)
    else:
        print('Pay amount is:',money)
