# 1.简单列表推导式 range步长
list1 = [i for i in range(0, 11, 2)]
print(list1)


# 2.for 循环加 if 创建有规律的列表
list2 = []
for i in range(11):
    if i % 2 == 0:
        list2.append(i)
    # i += 1
print(list2)


# 3.把 for 循环配合 if 的代码 改写 带 if 的列表推导式
list3 = [i for i in range(11) if i % 2 == 0]
print(list3)
