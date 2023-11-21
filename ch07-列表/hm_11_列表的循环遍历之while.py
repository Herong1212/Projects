name_list = ["Tom", "Lily", "Rose"]

"""
1. 准备表示下标数据
2. 循环 while
    条件 i < 3   len()
    遍历 -- 依次按顺序访问到序列的每一个数据
    i += 1
"""

i = 0
while i < len(name_list):   # 此处的 len 取得 3
    print(name_list[i])
    i += 1

print("遍历结束")
