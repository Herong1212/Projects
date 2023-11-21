"""
1. 书写input
    input("提示信息")

2. 观察特点
    2.1 遇到input, 等待用户输入
    2.2 接收input存变量
    2.3 input接收到的数据类型都是 字符串
"""

password = input("请输入您的密码: ")  # 用 password 接收 input输入的数据
print(f"您输入的密码为:{password}")

print(type(password))   # 验证 -- input接收到的数据类型都是 字符串



