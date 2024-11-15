# 1. float() -- 将数据转换成浮点型
num1 = 1
str1 = "10"
print(type((float(num1))))  # float
print(float(num1))   # 1.0

print(float(str1))   # 10.0

# 2. str() -- 将数据转换成字符串类型
print(type(str(num1)))

# 3. tuple() -- 将一个序列转换成元组
list1 = [10, 20, 30]
print(tuple(list1))     # 不用检测数据类型, 因为元组就是用的 ()

# 4. list() -- 将一个序列转换成列表
t1 = (100, 200, 300)
print(list(t1))         # 不用检测数据类型, 因为列表就是用的 []

# 5. eval() -- 计算在字符串串中的有效 Python 表达式, 并返回一个对象
str2 = "1"
str3 = "1.1"
str4 = "(1000, 2000, 3000)"
str5 = "[1000, 2000, 3000]"

print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))




