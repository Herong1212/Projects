# 多行多个乘法表达式 -- x * y = x*y
"""
1. 打印一个表达式: x * y = x*y
2. 一行打印多个表达式  --  一行表达式的个数和行号数相等  --  循环: 一个表达式  -- 不换行
3. 打印多个表达式  --  循环 :  一行表达式 -- 换行
"""

i = 1
while i <= 9:   # 行数
    # 一行的表达式开始
    j = 1
    while j <= i:  # 列数
        print(f'{j} * {i} = {i * j}', end='\t')
        j += 1
    # 一行的表达式结束
    print()
    i += 1
# 外层打印行数, 内层打印列数
