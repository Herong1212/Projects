# 需求: 1 - 100 数字累加和 -- 1 + 2 + 3 + 4 +... + 100 = 结果,  打印结果
"""
1. 准备做加法运算的数据  1 - 100 增量为1
2. 准备变量保存将来运算的结果
3. 循环做加法运算
4. 打印结果
5. 验证结果正确性
"""
#
# 准备数据
i = 1

# 准备结果变量
result = 0   # 因为还没开始做加法运算, 所以 result 初始化为 0

# 循环
while i <= 100:
    # 加法运算 前两个数的结果 + 第三个数 -- 每计算一次加法则更新一次 result 变量值
    result += i
    i += 1

# 打印最终结果
print(f'result = {result}')
