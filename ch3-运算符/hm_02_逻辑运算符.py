a = 0
b = 1
c = 2

# 1. and : 与 都真才有效
print((a < b) and (c > b))     # 如果表达式过于复杂，就加上小括号，可以提高优先级或者避免出现歧义（如下）

# print(a < b and c > b)         简单链式比较  可以优化成 -- a < b < c

print(a > b and c > b)

# 2. or : 或 一真则真，都假才假
print(a < b or c > b)
print(a > b or c > b)

# 3. not : 非 取反
print(not False)

print(not c > b)
