"""
三角形: 每行星星的个数和行号数相等
*
* *
* * *
* * * *
* * * * *
"""

i = 0
while i < 5:
    # 一行星星开始
    j = 0
    while j <= i:
        print('*', end=" ")
        j += 1
    # 一行星星结束:  换行显示下一行
    print()
    i += 1
