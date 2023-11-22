dict1 = {"name": "Tom", "age": 20, "gender": "男"}

# 1.[key]
# print(dict1["name"])   # 返回对应的值( key存在 )
# print(dict1["names"])  # 报错,不存在相应的key值

# 2. 函数
# 2.1 get()
# print(dict1.get('name'))
# print(dict1.get('id', 110))
# print(dict1.get('ids'))    # 如果key不存在 - 返回 None

# 2.2 keys() -- 查找字典中所有的 key, 返回可迭代对象
# print(dict1.keys())
#
# # 2.3 values()  --  查找字典中所有的 value , 返回可迭代对象
# print(dict1.values())

# 2.4 items()  --  查找字典中所有的 键值对 , 返回可迭代对象,  里面的数据是元组, 元组数据1是字典的key值,元组数据2是字典的value值
print(dict1.items())


