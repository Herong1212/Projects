dict1 = {"name": "Tom", "age": 20, "gender": "男"}

dict1["name"] = "Rose"
# 结果: {'name': 'Rose', 'age': 20, 'gender': '男'}
print(dict1)

# 字典序列[key] = 值
# id的值为110
dict1["id"] = 110
# 结果: {'name': 'Rose', 'age': 20, 'gender': '男', 'id': 110}
print(dict1)
