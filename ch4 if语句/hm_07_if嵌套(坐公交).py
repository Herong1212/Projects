# 坐公交: 如果有钱可以上车,没有钱,不能上车；  如果上车了,判断是否能坐下 --- 是否有空座位
"""
1. 准备将来要做判断的数据: 钱和空座
2. 判断是否有钱: 上车 和 不能上车
3. 上车了: 判断是否能坐下: 有空座位 和 无空座位
"""
money = 1
seat = 0

# 判断是否能上车
if money == 1:
    print(f'土豪, 请上车')

    # 判断是否能坐下
    if seat == 1:
        print(f'有空座,坐下了')
    else:
        print(f'没有空座,站着等......')
else:
    print(f'朋友,没带钱,跟着跑,跑快点')


"""
money = int(input("你有钱吗?"))

if money > 2:
    print(f'哦!你有{money}元, 可以上车了!')
    
    empty = int(input(f'你看看有几个空位?'))
    if empty > 0:
        print(f'还有{empty}个空位, 坐吧!')

    else:
        print(f'没位了, 你站着吧!')

elif money < 2:
    print(f'你都没钱,还想坐车?!')
    
"""
