# mystr = "hello world and itcast and itheima and Python"

# 1. capitalize() -- 字符串首字母大写
# 结果：Hello world and itcast and itheima and python
# new_str = mystr.capitalize()
# print(new_str)

# 2.title() -- 字符串中每个单词首字母大写
# 结果：Hello World And Itcast And Itheima And Python
# new_str = mystr.title()
# print(new_str)

# 3. lower() -- 大写转小写
# 结果：hello world and itcast and itheima and python
# new_str = mystr.lower()
# print(new_str)

# 4. upper() -- 小写转大写
# 结果：HELLO WORLD AND ITCAST AND ITHEIMA AND PYTHON
# new_str = mystr.upper()
# print(new_str)

mystr = "   hello world and itcast and itheima and Python   "
print(mystr)

# 1. lstrip() --
new_str = mystr.lstrip()
# 结果:hello world and itcast and itheima and Python
print(new_str)

# 2. rstrip() --
new_str2 = mystr.rstrip()
# 结果:   hello world and itcast and itheima and Python
print(new_str2)

# 3. strip() --
new_str3 = mystr.strip()
# 结果:hello world and itcast and itheima and Python
print(new_str3)
