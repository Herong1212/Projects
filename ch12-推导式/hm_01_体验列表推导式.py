# 需求：0,1.2，3 . . .
#  1.循环实现  2.列表推导式（化简代码：创建或控制有规律的代码）
"""
1.1 创建空列表
1.2 循环将有规律的数据写入列表
"""

# while 实现-----------------
# list1 = []
#
# i = 0
# while i < 11:
#     list1.append(i)
#     print(list1[i], end=' ')
#     i += 1
# print()
# print(list1)

# for 实现--------------------
# list1 = []
# for i in range(0, 11, 1):
#     list1.append(i)

# print(list1)

# 列表推导式实现------------------------
list1 = [i for i in range(10)]       # for 左边的 i 是返回值的意思！
print(list1)
