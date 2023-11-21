str1 = 'itheima'
for i in str1:
    # 当某些条件成立退出循环  --  break: 条件 i 取到字符 e
    if i == 'e':
        print('遇到e不打印')
        break
    print(i)
