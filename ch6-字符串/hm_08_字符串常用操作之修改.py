mystr = "hello world and itcast and itheima and Python"

# replace 把 and 换成 he    #** 说明 replace 函数有返回值，返回值是修改后的字符串
new_str = mystr.replace('and', 'he')

new_str = mystr.replace('and', 'he', 2)

# 替换次数如果超过子串出现次数，表示替换所有这个子串
new_str = mystr.replace('and', 'he', 20)

print(mystr)
print(new_str)
# ***** 调用了 replace 函数后，发现原有字符串的数据并没有做到修改，修改后的数据是 replace 函数的返回值
# --- 说明 字符串是不可变数据类型
# 数据是否可变 划分为   可变类型 和 不可变类型


# 2. split() -- 分割，返回一个 列表，丢失分割字符
# 结果：['hello world ', ' itcast ', ' itheima ', ' Python']
list1 = mystr.split('and')
# 结果：['hello world ', ' itcast ', ' itheima and Python']
list2 = mystr.split('and',2)
# 结果：['hello', 'world', 'and', 'itcast', 'and', 'itheima', 'and', 'Python']
list3 = mystr.split(' ')
# 结果：['hello', 'world', 'and itcast and itheima and Python']
list4 = mystr.split(' ',2)
print(list1)
print(list2)
print(list3)
print(list4)


# 3. join() -- 合并列表里面的字符串数据为一个大字符串
mylist = ['aa', 'bb', 'cc']

# 输出显示 -- aa...bb...cc
list1 = ['chuan', 'zhi', 'bo', 'ke']
t1 = ('aa', 'bb', 'cc', 'ddd')
# 结果：aa...bb...cc
new_str = '...'.join(mylist)     # ... 也可以换成别的字符
print(new_str)
# 结果：chuan_zhi_bo_ke
new_str2 = '_'.join(list1)
print(new_str2)
