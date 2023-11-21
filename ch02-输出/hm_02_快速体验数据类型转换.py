"""
1. input

2. 检测input数据类型

3. int() 转换数据类型

4. 检测是否转换成功
"""
num = input("请输入数字: ")
print(f'您输入的数字为: ')

print(type(num))  # str

print(type(int(num)))  # int
