# Runde Jia
# Sydeney
# 2021/11/19 22:11
s='hello.python'
print('1.',s.isidentifier())
print('2.','hello'.isidentifier())
print('3','zhangsan_'.isidentifier())
print('4.','zhangsan_123'.isidentifier())

print('5.','\t'.isspace())
print('6.','abc'.isalpha())
print('7.','张三'.isalpha())
print('8.','zhangsan1'.isalpha())

print('9','123'.isdecimal())
print('10','123four'.isdecimal())
print('11','123'.isnumeric())
print('11','123四'.isnumeric())

print('15.','abc1'.isalnum())
print('16.','张三123'.isalnum())
print('17.','abc'.isalnum())
print('18.','abc%'.isalnum())