a = 0
b = 1
c = 2

# and 运算符, 只要有一个值为 0, 则结果为 0, 否则结果为最后一个非 0 数字
print(a and b)  # 0
print(b and a)  # 0
print(a and c)  # 0
print(c and a)  # 0
print(b and c)  # 2
print(c and b)  # 1

print("---------------")

# or 运算符, 只有所有值都为 0 结果才为 0, 否则结果为第一个非 0 数字
print(a or b)  # 1      a 为 0, 所以返回第一个非 0 数字, 即 返回 b
print(a or c)  # 2
print(b or c)  # 1

