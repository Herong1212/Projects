"""
语法:
    条件成立执行的表达式  if  条件  else  条件不成立执行的表达式
"""

a = 1
b = 2

c = a if a > b else b
print(c)

# 需求:  有两个变量, 比较大小  如果变量1 大于 变量2 执行 变量1 - 变量2;  否则  变量2 - 变量1
num1 = 20
num2 = 40
var = (num1 - num2) if (num1 > num2) else (num2 - num1)
print(var)
