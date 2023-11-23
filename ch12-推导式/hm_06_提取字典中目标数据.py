counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}

# 1.需求：提取上述电脑数量大于等于 200 的字典数据
# 获取所有键值对数据，判断 v 值是否大于等于 200  返回 字典
count1 = {k: v for k, v in counts.items() if v >= 200}
print(count1)
