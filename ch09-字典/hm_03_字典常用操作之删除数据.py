dict1 = {"name": "Tom", "age": 20, "gender": "男"}

# del() / del : 删除字典或删除字典中指定的键值对
# del(dict1)
# print(dict1)

# del dict1["name"]
# del dict1["names"]   # 报错
# 结果: {'age': 20, 'gender': '男'}
# print(dict1)

# clear() : 清空字典
dict1.clear()
print(dict1)
