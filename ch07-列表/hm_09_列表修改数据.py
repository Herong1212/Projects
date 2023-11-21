name_list = ["Tom", "Lily", "Rose"]

# 1.修改指定下标的数据
# name_list[0] = "aaa"
# print(name_list)

# 2.逆置 reverse()
list1 = [1, 3, 2, 5, 4, 6]
list1.reverse()
print(list1)

# 3.sort() -- 排序 : 升序(默认) 和 降序
# list1.sort()
list1.sort(reverse=True)

# 结果 : [1, 2, 3, 4, 5, 6]
print(list1)

