name_list = ["Tom", "Lily", "Rose"]

# 需求: 注册邮箱, 用户输入一个帐号名, 判断这个帐号是否存在, 若存在,提示用户;否则提示可以注册
"""
1.用户输入帐号
2.判断 if...else...
"""

name = input("请输入您的名字: ")
print(f'您输入的名字为:{name}')

if name in name_list:
    # 提示用户名已经存在
    print("The name you input has exists !")
else:
    # 提示可以注册
    print("input successful!")


