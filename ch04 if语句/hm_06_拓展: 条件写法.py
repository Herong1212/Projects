"""
m_age = input("请输入您的年龄: ")
age = int(m_age)
"""

age = int(input('请输入您的年龄: '))

# 童工
if age < 18:
    print(f'您输入的年龄为: {age}, 是童工,不敢用您')

# 18-60 合法工龄
elif 18 <= age <= 60:  # 尽量不要使用连续大于小于这样的结构, 容易被误解
    print(f'您输入的年龄为: {age}, 合法工作年龄,恭喜您,打工人!')

# 大于60 退休
elif age > 60:
    print(f'您输入的年龄为: {age}, 该退休啦')


