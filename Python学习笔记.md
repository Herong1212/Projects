# 课程：Python入门



cmd 进去之后，输入python，回车可进入版本，要更换版本：

输入 exit（），回车

输入python3，回车，

即可进入3版本开头的python版本。





## 一.  初识

1. 更改单行注释颜色

​	Preferences --> Editor --> Corlor Scheme --> Python -- Line Comment

2. 更改多行注释颜色

   Preferences --> Editor --> Corlor Scheme --> Python --Docstring --> Text

3. 更改string颜色

   Preferences --> Editor --> Corlor Scheme --> Python --String --> Text





## 课程:   注释及变量



### 1.  格式化符号基础使用用法

1. 要保留几位小数，就在%和f之间加  .要保留的小数位数， 如.2保留2位小数， .3保留3位小数

2. 表示输出的整数显示位数，不足以0补全，超出当前位数则原样输出
3. 需要传入多个数据时，用 ， 隔开每个数据



### 2.  输出 f -- 格式化字符串

```
name = "Tom"
age = 18
# 语法: f'{字符串} '
print(f'我的名字是{name}, 今年{age}岁了')
```



### 3.  转义字符

1.  \n -- 换行              

    注意:  print()自带换行功能

2.  \t -- 制表符, 一个tab键( 4个空格 )的距离





### 4.  PyCharm交互式开发(待处理)

1. 只能用于简单测试, 并且只是临时存储数据
2.  正常业务开发必须建立 .py 文件





## 课程:  输入

目标

- 输入功能的语法
- 输入 input 的特点



### 1.  算术运算符

// --- 整除    	eg: 9 // 4 = 2

** --- 指数   	eg: 2 ** 4 = 2 * 2 * 2 * 2 = 16

() --- 小括号  	eg: 小括号用来提高运算优先级, 即(1 + 2) * 3 的输出结果为 9



注意: 

​	混合运算优先级顺序:   ( )   高于  **   高于   /   //   %   高于   +   -

​	2 * 0.5 = 1.0           4 / 2 = 2.0



### 2.  赋值运算符

1. 单个变量赋值

   

2. 多个变量赋值

```
num1, num2, str1 = 1, 1.1, "abc"
print(num1)
print(num2)
print(str1)
```



3. 多变量赋相同值

```
a = b = 10
print(a)
print(b)
```



### 3.  复合赋值运算符

+=   先执行前面的 + ,  然后执行赋值,  如 c += a  等价于  c = c + a

```
#  注意: 先算复合赋值运算符右边的表达式； 再算复合赋值运算
d *= 1 + 2                                 # d = d * ( 1 + 2 )
```



### 4.  比较运算符



### 5.  逻辑运算符

| 运算符 | 逻辑表达式 | 描述                                                         | 实例                                     |
| ------ | ---------- | ------------------------------------------------------------ | ---------------------------------------- |
| and    | x and y    | 布尔"与": 如果 x 为 False,  x and y 返回 False,  否则返回 y 的值 | True and False,  返回 False              |
| or     | x or y     | 布尔"或": 如果 x 为 True,  返回 True,  否则返回 y 的值       | False and True,  返回 True               |
| not    | not x      | 布尔"非": 如果 x 为 True,  返回 False.  如果 x 为 False,  返回 True | not True 返回 False,  not False 返回True |



书写习惯: 

```
print((a < b) and (c > b))     # 如果表达式过于复杂，就加上小括号，可以提高优先级或者避免出现歧义（如下）

# print(a < b and c > b)         简单链式比较  可以优化成 -- a < b < c
```

即 : 加小括号提高优先级, 或避免歧义



#### 5.1  拓展 --- 数字的逻辑运算

```
# and 运算符, 只要有一个值为 0, 则结果为 0, 否则结果为最后一个非 0 数字
print(a and b)  # 0
print(b and a)  # 0
print(a and c)  # 0
print(c and a)  # 0
print(b and c)  # 2
print(c and b)  # 1

print("---------------")

# or 运算符, 只有所有值都为 0 结果才为 0, 否则结果为第一个非 0 数字
print(a or b)  # 1      a 为 0, 所以返回第一个非 0 数字, 即 返回 b
print(a or c)  # 2
print(b or c)  # 1
```





## 课程:  条件语句



### 1.  了解条件语句



### 2.  if 语法

#### 2.1 语法	

```
if 条件:
    条件成立执行的代码1
    条件成立执行的代码2
    ......
```



#### 2.2 快速体验

```
if True:
    print("条件成立执行的代码1")
    print("条件成立执行的代码1")

# 注意: 在这个下方的没有加缩进的代码  不属于 if 语句块, 即和条件成立与否无关
print("我是无论条件是否成立都要执行的代码")
```



### 3.  实例:  上网

需求分析: 如果用户年龄大于等于18岁, 即成年, 输出" 已经成年, 可以上网"

#### 3.1 简单版: 网吧上网

```
# 分析: 年龄大于等于18, 输出: 已经成年, 可以上网 --- 准备年龄的数据 和 18 做比较
age = 20

if age >= 18:
    print(f'已经成年,可以上网')

print(f'系统关闭')
```



#### 3.2 进阶版: 网吧上网

新增需求: 用户可以输出自己的年龄, 然后系统进行判断是否成年, 成年则输出"您的年龄是'用户输入的年龄', 已经成年,可以上网了".

```
# input接收用户输入的数据是字符串类型, 条件是 age 和 整型 18 做判断, 所以这里要 int 转换数据类
型
m_age = input("请输入您的年龄: ")
age = int(m_age)                       # int(m_age)   是错误的,  数据转换类型函数要有接收值, 如本例中的age

# age = int(input("请输入您的年龄: "))  也可以

if age >= 18:
    print(f'您的年龄是{age}, 已经成年, 可以上网了哦')

print(f'系统关闭')
```



### 4.  if...else...

作用: 条件成立执行 if 下方的代码;  条件不成立执行 else 下方的代码.

#### 4.1 语法

```
if 条件:
    条件成立执行的代码1
    条件成立执行的代码2
    ......
else:
    条件不成立执行的代码1
    条件不成立执行的代码2
    ......
```



#### 4.2 实用版: 网吧上网

```
m_age = input("请输入您的年龄: ")
age = int(m_age)

# age = int(input("请输入您的年龄: "))  也可以

if age >= 18:
    print(f'您的年龄是{age}, 已经成年, 可以上网了哦')
else:
    print(f'您的年龄是{age}, 还未成年, 上什么网!')

print("系统关闭")
```



### 5.  多重判断

思考: 中国合法工作年龄为18-60周岁, 即如果年龄小于18的情况视为童工, 不合法;  如果年龄在18-60岁之间为合法工龄;  大于60岁为法定退休年龄.



#### 5.1 语法

```
if 条件1:
    条件1成立执行的代码1
    条件1成立执行的代码2
    ......
elif 条件2
    条件2成立执行的代码1
    条件2成立执行的代码2
    ......
......
else:
    以上条件都不成立执行的代码
```

多重判断也可以和 else 配合使用.  一般 else 放到最后整个 if 语句的最后,  表示以上条件都不成立的时候执行的代码.



#### 5.2 实例: 工龄判断

```
age = int(input('请输入您的年龄: '))
if age < 18:
		print(f'您输入的年龄为: {age}, 是童工,不敢用您')
elif (age >= 18) and (age <= 60):
 	    print(f'您输入的年龄为: {age}, 合法工作年龄,恭喜您,打工人!')
elif- age > 60:
    	print(f'您输入的年龄为: {age}, 该退休啦')
```

拓展:  `(age >= 18) and (age <= 60)  可以简化为 18  <=  age  <=  60`.



### 6.  if 嵌套

思考 : 坐公交 : 如果有钱可以上车,  没钱不能上车;  上车后如果有空座,  则可以坐下;  如果没有空座,  就要站着.  怎样写程序?



#### 6.1 语法

```
if 条件1:
	条件1成立执行的代码1
	条件1成立执行的代码2

		if 条件2:
			条件2成立执行的代码
			条件2成立执行的代码
			
```

注意:  条件2的 if 也是出于条件1的缩进关系内部



#### 6.2   实例: 坐公交



### 7.  应用: 猜拳游戏

需求分析: 

-   参与游戏的角色

​		玩家

​			手动出拳

​		电脑

​			随机出拳

-   判断输赢

​		玩家获胜

| 玩家 | 电脑 |
| ---- | ---- |
| 石头 | 剪刀 |
| 剪刀 | 布   |
| 布   | 石头 |

​		平局

​			玩家出拳 和 电脑出拳相同

​		电脑获胜



随机做法: 

1.   导入 random 模块

     `import 模块名`

2.   使用 random 模块中的==随机整数==功能

     `random.randint (开始, 结束)`



```
"""
提示:  0 - 石头,  1 - 剪刀,  2 - 布

1. 出拳
    玩家: 手动输入出拳
    电脑: 1. 固定出拳 :  剪刀;       2. 随机出拳
    
2. 判断输赢
    2.1 玩家获胜
    2.2 平局
    2.3 电脑获胜
"""

3 导入 random 模块
import random      # 一般把导模块代码放在所有业务逻辑代码最前面,为了接下来的所有代码都有权限来使用该模块

# 计算电脑出拳的随机数字
num = random.randint(0,2)
print( computer )


player = int(input('请出拳: 0 -- 石头; 1 -- 剪刀; 2 -- 布; '))

# computer = num
computer = random.randint(0,2)
print(f'电脑出的是{computer}')

# 玩家获胜  p0 : c1  或  p1 : c2  或  p2 : c0
if (player == 0) and (computer == 1) or (player == 1) and (computer == 2) or (player == 2) and (computer == 0):
    print(f'玩家获胜, 哈哈哈哈!')

# 平局
elif player == computer:
    print(f'平局! 别走, 再来一局!')

# 电脑获胜
else:
    print(f'很遗憾,您输了!')
    
```



### 8.  三目运算符

三目运算符也叫三元运算符或三元表达式

语法如下: 

`条件成立执行的表达式  if  条件  else  条件不成立执行的表达式`

快速体验:  

```
a  = 1

b = 2



c = a if a > b else b

print(c)
```



### 总结

-   if 语句语法

    ```
    if 条件:
        条件成立执行的代码1
        条件成立执行的代码2
        ......
    ```

    

-   if ... else ...

    ```
    if 条件:
        条件成立执行的代码1
        条件成立执行的代码2
        ......
    else:
        条件不成立执行的代码1
        条件不成立执行的代码2
        ......
    ```

    

-   多重判断

    ```
    if 条件1:
            条件1成立执行的代码1
            条件1成立执行的代码2
            ......
    elif 条件2
            条件2成立执行的代码1
            条件2成立执行的代码2
            ......
        ......
    else:
            以上条件都不成立执行的代码
    
    ```

    if 嵌套

    	if 条件1:
    		条件1成立执行的代码1
    		条件1成立执行的代码2
    		......
    			if 条件2:
    				条件2成立执行的代码
    				条件2成立执行的代码
    				......

-   三目运算符

`条件成立执行的表达式  if  条件  else  条件不成立执行的表达式`





## 课程:  循环

目标

-   了解循环
-   while 语法 [重点]
-   while 应用
-   break 和 continue
-   while 循环嵌套 [重点]
-   whille 循环嵌套应用 [难点]
-   for 循环



### 1.  循环简介

#### 1.1 循环的作用

```
思考:  假如我有个女朋友，有一天我们闹矛盾生气了，女朋友说:道歉，说100遍“媳妇儿，我错了”。这个时候程序员会怎么做?

答:  100遍 print( '媳妇儿，我错了')

思考:  复制粘贴100次吗?

答:  重复执行100次一样的代码，程序中循环即可
```

循环的作用:  让代码更高效的重复执行.



#### 1.2 循环的分类

在 Python 中,  循环分为 `while` 和 `for` 两种



### 2.  while 的语法

```
while 条件:
    条件成立执行的代码1
    条件成立执行的代码2
    ......
```



#### 2.1 快速体验

需求:  复现重复执行100次 `print( ' 媳妇儿我错了 ')`  (输出更简洁一些, 我们这里设置5次) .

分析:  初始值是0次,  终点是5次,  重复做的事情 --- 输出 ' 媳妇儿我错了 ' .

```
# 循环的计数器
i = 0
while i <= 5:
    print(f'媳妇儿, 我错了')
    i += 1
    
print('任务结束')
```



#### 2.2 计数器书写习惯



### 3.  循环的应用

#### 3.1 应用一:  计算 1 - 100 累加和

分析:  1 - 100 的累加和,  即 1 + 2 + 3 + 4 + ... ,  即前两个数字的相加结果 + 下一个数字 ( 前一个数字 + 1 ).

```
i = 1

# 准备结果变量
result = 0   # 因为还没开始做加法运算, 所以 result 初始化为 0

# 循环
while i <= 100:
    # 加法运算 前两个数的结果 + 第三个数 -- 每计算一次加法则更新一次 result 变量值
    result += i
    i += 1

# 打印最终结果 -- 5050
print(f'result = {result}')
```

注意:  为了验证程序的准确性, 可以先改小数值,  验证结果正确后,  再改成 1 -100 做累加



#### 应用二:  计算 1 - 100 偶数累加和

分析:  1 - 100 的偶数和,  即 2 + 4 + 6 + 8 + ......,  得到偶数的方法如下:  

-   偶数即是和 2 取余结果为 0 的数字,  可以加入条件语句判断是否为偶数,  为偶数则累加
-   初始值为 0 / 2,  计数器每次累加 2



##### 3.2.1 方法一:  条件判断和 2 取余数则累加

```
# 方法一:  条件判断和 2 取余数为 0 则累加计算
i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1  # 写在  while 里面的
    
# 输出 2550
print(f'result = {result}')
```



##### 3.2.2 方法二:  计数器控制

```
# 方法二: 计数器控制增量为 2
i = 0  # 也可以从 2 开始
result = 0
while i <= 100:
    result += i
    i += 2
    
# 输出 2550
print(result)
```



### 4.  break 和 continue

break 和 continue 是循环中满足一定条件退出循环的两种方式.



#### 4.1  理解

举例:  一共吃5个苹果，吃完第一个，吃第二个...，这里"吃苹果"的动作是不是重复执行?

情况一:  如果吃的过程中，吃完第三个吃饱了，则不需要再吃第4个和第5个苹果，即是吃苹果的动作停止，这里就是`break`控制循环流程，即==终止此循环==。

情况二:  如果吃的过程中，吃到第三个吃出一个大虫....，是不是这个苹果就不吃了，开始吃第四个苹果，这里就是`continue`控制循环流程，即==退出当前一次循环继而执行下一次循环代码==。



##### 4.1.1  情况一:  break

```
i = 1
while i <= 5:
    # 条件: 如果吃到 4 或 >3  打印 " 吃饱了, 不吃了"
    if i == 4:
        print(f'吃饱了,不吃了')
        break
    print(f'吃了第{i}个苹果')
    i += 1
```



##### 4.2.2  情况二:  continue

```
i = 1

while i <= 5:

    if i == 3:
    
        print("吃出一条大虫子,这个苹果不吃了")
        
        # 如果要用 continue , 在continue之前一定要修改计数器,否则进入死循环
        
        i += 1
        
        continue
        
    print(f'吃了第{i}个苹果')
    
    i += 1
```



### 5.  while 循环嵌套

#### 5.1  应用场景

故事梗概: 有天女朋友生气了,  惩罚:  说3遍" 媳妇儿,  我错了 ",  这个程序是不是循环即可?  但如果女朋友说:  还要刷今天晚饭的碗,  这个程序怎样写?

```
while 条件:

		print("媳妇儿,  我错了")

print("刷晚饭的碗")
```

但如果女朋友还是生气,  把这套惩罚要连续3天执行,  又如何书写程序?

```
while 条件:

    	while 条件:
    
        		print('媳妇儿, 我错了')
        
    	print('刷晚饭的碗')
```

#### 5.2  语法

```
while 条件1:
  	 	条件1成立执行的代码
    	......
   		 while 条件2:
        		条件2成立执行的代码
       			 ......
        
```

总结:  所谓 while 循环嵌套,  就是一个 while 里面嵌套一个 while 的写法,  每个 while 和之前的基础语法是相同的



#### 5.3  快速体验:  复现场景

##### 5.3.1  代码

```
j = 0
while j < 3:
    i = 0
    while i < 3:
        print("媳妇儿, 我错了")
        i += 1
    print(f'刷晚饭的碗')
    print(f'一套惩罚结束-------------------')
    j += 1
```



##### 5.3.2  执行结果



##### 5.3.3 理解执行流程

当内部循环执行完成之后, 在执行下一次外部循环的条件判断![](/home/ghr/图片/py教程/理解循环执行流程.png)



### 6.  while 循环嵌套应用

#### 6.1  应用一:  打印星号(正方形)

##### 6.1.1  需求

```
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```



##### 6.1.2  代码

分析:  一行输出5个星号,  重复打印5行

```
# 重复打印 5 行星星
i = 0
while i < 5:
	# 一行星星的打印
    j = 0
    while j < 5:
    # 一行内的星星不能换行,  取消 print() 默认结束符 \n
        print(f'*', end=' ')    # print()默认有自动换行符,  要想横着输出,  需要把 \n 删除,  即换成空格
        j += 1
    # 每行结束要换行,  这里借助一个空的 print() ,  利用 print() 默认结束符换行 
    print()                      #  即print(end='\n')
    i += 1
```



#### 6.2  应用二:  打印星号(三角形)

##### 6.2.1  需求

```
*
* *
* * * 
* * * *
* * * * * 
```



##### 6.2.2  代码

分析:  ==一行输出星星的个数和行号是相等的==,  每行:  重复打印行号数字个星星,  将打印行星号的命令重复执行5次实现打印5行.

```
# 重复打印5行星星
# i 表示行号
i = 0
while i < 5:
    # 一行星星开始
    j = 0
    # j 表示每行星星里面星星的个数,  这个数字要和行号相等,  所以 j 要和 i 联动
    while j <= i:
        print('*', end=" ")
        j += 1
    # 一行星星结束:  换行显示下一行
    print()
    i += 1
```



#### 6.3  九九乘法表

##### 6.3.1  执行结果

![image-20231117170127761](/home/ghr/图片/py教程/九九乘法表.png)



##### 6.3.2  代码

```
# 重复打印 9 行表达式
i = 1
while i <= 9:            # 行数
    # 一行的表达式开始,  打印一行里面的表达式 a * b = a*b
    j = 1
    while j <= i:          # 列数
        print(f'{j} * {i} = {i * j}', end='\t')
        j += 1
    # 一行的表达式结束
    print()
    i += 1
```



### 7.  for 循环

#### 7.1  语法

```
for 循环变量 in 序列
    重复执行的代码1
    重复执行的代码2
    ......
```



#### 7.2  快速体验

```
str1 = "itheima"
for i in str1:
    print(i)
```



执行结果:

![](/home/ghr/图片/py教程/for 循环体验.png)



#### 7.3  break

```
str1 = 'itheima'
for i in str1:
    # 当某些条件成立退出循环  --  break: 条件 i 取到字符 e
    if i == 'e':
        print('遇到e不打印')
        break
    print(i)
```



执行结果:

![](/home/ghr/图片/py教程/for循环之break.png)



#### 7.4  continue 

```
str1 = 'itheima'
for i in str1:
    # 当某些条件成立退出循环  --  continue: 条件 i 取到字符 e
    if i == 'e':
        print('遇到e不打印')
        continue
    print(i)
```



执行结果:

![](/home/ghr/图片/py教程/for循环之continue.png)



### 8.  else

循环可以和 else 配合使用,  else 下方缩进的代码指的是==当循环正常结束之后要执行的代码==.

#### 8.1  while...else...

需求:  女朋友生气了,  要惩罚:  连续说 5 遍 "媳妇儿,  我错了" ,  如果道歉正常完毕女朋友就原谅我了,  这个程序怎样写?

```
i = 1
while i <= 5:
    print('媳妇儿. 我错了')
    i += 1
else:
    print('媳妇儿原谅我了...')
```

思考:  这个 print() 是不是没有循环也能执行?



##### 8.1.1  语法

```
while 条件:

​	条件成立执行的代码

else:

​	循环正常结束之后要执行的代码
```



##### 8.1.2  示例



##### 8.1.3  退出循环的方式

需求:  女朋友生气,  要求道歉 5 遍:  媳妇儿,  我错了.  道歉到第三遍的时候,  媳妇儿埋怨这一遍说的不真诚,  是不是就要退出循环了?  这个退出有两种可能:  

- 更生气了,  不打算原谅,  也不需要道歉了,  程序如何书写?
- 只一遍不真诚,  可以忍受,  继续下一遍道歉,  程序如何书写? 



1.    break

```
i = 1
while i <= 5:
    if i == 3:
    print('这遍说的不真诚')
        break
    print('媳妇儿. 我错了')
    i += 1
else:
    print('媳妇儿原谅我了, 真开心呐, 哈哈哈')
```

![](/home/ghr/图片/py教程/while...else之break.png)

```
所谓 else 指的是循环正常结束之后要执行的代码,  即如果是 break 终止循环的情况,  else 下方缩进的代码将不再执行
```



2.   continue

```
i = 1
while i <= 5:
    if i == 3:
        print('这遍说的不真诚')
        i += 1
        continue
    print('媳妇儿. 我错了')
    i += 1
else:
    print('媳妇儿原谅我了, 真开心呐, 哈哈哈')
     
```

![](/home/ghr/图片/py教程/while...else之continue.png)

```
因为 continue 是退出当前一次循环,  继续下一次循环,  所以该循环在 continue 控制下是可以正常结束的,  当循环结束后,  则执行了 else 缩进的代码
```



#### 8.2  for ... else ...

##### 8.2.1  语法

```
for  临时变量 in 序列:
		重复执行的代码
        ...
else:
		循环正常结束之后要执行的代码
```

```
所谓 else 指的是循环正常结束之后要执行的代码,  即如果是 break 终止循环的情况,  else 下方缩进的代码将不执行
```



##### 8.2.2  示例

```
str1 = "itheima"
for i in str1:
    print(i)
else:
    print('循环正常结束之后执行的代码')

```



##### 8.2.3  退出循环的方式

1.  break

```
str1 = "itheima"
for i in str1:
    if i == 'e':
        print('遇到e不打印')
        break 
    print(i)
else:
    print('循环正常结束之后执行的代码')
    
```

执行结果:	![image-20231118161731811](/home/ghr/.config/Typora/typora-user-images/image-20231118161731811.png)

```
没有执行 else 缩进的代码
```



2. continue 控制循环

    ```
    str1 = "itheima"
    for i in str1:
        if i == 'e':
            print('遇到e不打印')
            continue
        print(i)
    else:
        print('循环正常结束之后执行的代码')
        
    ```

执行结果:

![](/home/ghr/图片/py教程/for...else之continue.png)

```
因为 continue 是退出当前一次循环,  继续下一次循环,  所以该循环在 continue 控制下是可以正常结束的,  当循环结束后,  则执行了 else 缩进的代码
```



### 总结

- 循环的作用:  控制代码重复执行
- while 语法

```
while 条件:
    条件成立执行的代码1
    条件成立执行的代码2
    ......
```

- while 循环嵌套语法

```
while 条件1:
  	 	条件1成立执行的代码
    	......
   		 while 条件2:
        		条件2成立执行的代码
       			 ......  
```

- for 循环语法

    ```
    for 循环变量 in 序列
        重复执行的代码1
        重复执行的代码2
        ......
    ```

- break 退出整个循环

- continue 退出本次循环,  继续执行下一次重复执行的代码

- else 

    - while 和 for 都可以配合 else 使用
    - else 下方缩进代码的含义:  当循环正常结束后执行的代码
    - break 终止循环不会执行 else 下方缩进的代码
    - continue 退出循环的方式会执行 else 下方缩进的代码





## 课程:  字符串

目标

- 认识字符串
- 下标
- 切片
- 常用操作方法



### 一.  认识字符串

字符串是 Python 中最常用的数据类型.   我们一般用引号来创建字符串.  创建字符串很简单,  只需要为变量分配一个值即可.

```
a = 'hello world'

b = "abcdefg"

print(type(a))

print(type(b))
```

注意:  控制台显示结果为 `<class 'str'>`,  即数据类型为 str (字符串)



#### 1.1  字符串特征

- 一对引号字符串

```
name1 = 'Tom'

name2 = "Rose"
```



- 三引号字符串

```
name3 = '''Tom'''

name4 = """Rose"""

a = '''i am Yom,  nice to meet you!'''

b = """i am Rose,   nice to meet you!"""


```

注意:  三引号形式的字符串支持换行

思考:  如果创建一个字符串 `I'm Tom` ?

```
c = "I'm Tom"

d = 'I\'m Tom'
```



#### 1.2  字符串输出

```
print('hello world')

name = 'Tom'
print('我的名字是%s' % name)
print(f'我的名字是{name}')
```



#### 1.3  字符串输入

在 Python 中,  使用 input 接收用户输入

- 代码

```
name = input('请输入您的名字: ')
print(f'您输入的名字是: {name}')
print(type(name))
```



### 四.  常用操作方法

字符串的常用操作方法有查找,  修改和判断三大类

##### 4.1  查找

所谓字符串查找方法即是查找子串在字符串中的位置或出现的次数.

- ==find()== :  检测某个子串是否包含在这个字符串中,  如果在返回这个子串开始的下标,  否则则返回 -1.

    1. 语法

        ```
        字符串序列.find(子串,开始位置下标,结束位置下标)
        ```

        注意:  开始和结束位置下标可省略,  表示在整个字符串序列中查找

        

    2. 快速体验

        ```
        mystr = "hello world and itcast and itheima and Python"
        
        print(mystr.find('and'))   # 12
        print(mystr.find('and',15,30))  # 23
        print(mystr.find('ands'))  # -1
        ```

        

- ==index()== :  检测某个子串是否包含在这个字符串中,  如果在返回这个子串开始的位置下标,  否则则报异常.

    1. 语法

        ```
        字符串序列.index(子串,开始位置下标, 结束位置下标)
        ```

        注意:  开始和结束位置可省略,  表示在整个字符串序列中查找.

    

    2.   快速体验

         ```
         mystr = "hello world and itcast and itheima and Python"
         
         print(mystr.index('and'))   # 12
         print(mystr.index('and',15,30))  # 23
         print(mystr.index('ands'))  # 报错
         
         ```

    

- ==rfind()== :  和 find() 功能相同,  但查找方向为==右侧==开始

    

- ==rindex()== :  和 index() 相同,  但查找方向为==右侧==开始

    

- ==count()== :  返回某个子串在字符串中出现的次数

    1. 语法

        ```
        字符串序列.count(子串,开始位置下标,结束位置下标)
        ```

        注意:  开始和结束位置可省略,  表示在整个字符串序列中查找.

        

    2. 快速体验

        ```
        mystr = "hello world and itcast and itheima and Python"
        
        print(mystr.count('and'))  # 3
        print(mystr.count('and',15, 30))  # 1
        print(mystr.count('ands'))  # 0
        ```



##### 4.2  修改

所谓修改字符串,  指的就是通过函数的形式修改字符串中的数据.

- ==replace()== : 

  1. 语法：

     ```
     字符串序列.replace(旧字串，新字串，替换次数)
     ```

     注意：替换次数如果查出子串出现次数，则替换次数为该子串出现次数

  

  2. 快速体验

     ```
     mystr = "hello world and itcast and itheima and Python"
     
     # replace 把 and 换成 he    #** 说明 replace 函数有返回值，返回值是修改后的字符串
     new_str = mystr.replace('and', 'he')
     new_str = mystr.replace('and', 'he', 2)
     
     # 替换次数如果超过子串出现次数，表示替换所有这个子串
     new_str = mystr.replace('and', 'he', 20)
     ```

     注意：数据按照是否能直接修改分为可变类型和不可变类型两种。字符串类型的数据修改的时候不能改变原有字符串，属于不能直接修改数据的类型，即是不可变类型。

  

- ==split()== :   按照指定字符分割字符串

  1. 语法：

     ```
     字符串序列.split(分割字符，num)
     ```

     注意：num 表示的是份分割字符出现的次数，即将来返回数据个数为 num+1.

     

  2. 快速体验

      ```
      mystr = "hello world and itcast and itheima and Python"
      
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
      ```

      注意：如果分割字符是原有字符串中的子串，分割后则丢失该子串




- ==join()== :  用一个字符或子串合并字符串，即是将多个字符串合并为一个新的字符串。

  1. 语法：

     ```
     字符或子串.join(多字符串组成的序列)
     ```

     

  2. 快速体验

     ```
     list1 = ['chuan', 'zhi', 'bo', 'ke']
     t1 = ('aa', 'bb', 'cc', 'ddd')
     # 结果：aa...bb...cc
     new_str = '...'.join(mylist)     # ... 也可以换成别的字符
     print(new_str)
     # 结果：chuan_zhi_bo_ke
     new_str2 = '_'.join(list1)
     print(new_str2)
     
     ```

  

- capitalize() :  将字符串第一个字符转换成大写。

  1. 快速体验

      ```
      mystr = "hello world and itcast and itheima and Python"
      
      # 结果：Hello world and itcast and itheima and python
      new_str = mystr.capitalize()
      print(new_str)
      ```

      注意：capitalize() 函数转换后，只字符串第一个字符大写，其他的字符全都小写。

  

- title() : 将字符串每个单词首字母转换成大写。

  1. 快速体验

      ```
      mystr = "hello world and itcast and itheima and Python"
      
      # 结果：Hello World And Itcast And Itheima And Python
      new_str = mystr.title()
      print(new_str)
      ```

  

- lower() : 将字符串中所有字符大写转小写。

  1. 快速体验

      ```
      mystr = "hello world and itcast and itheima and Python"
      
      # 结果：hello world and itcast and itheima and python
      new_str = mystr.lower()
      print(new_str)
      ```

  

- upper() : 将字符串中所有字符小写转大写。

  1. 快速体验
  
      ```
      mystr = "hello world and itcast and itheima and Python"
      
      # 结果：HELLO WORLD AND ITCAST AND ITHEIMA AND PYTHON
      new_str = mystr.upper()
      print(new_str)
      ```
  
      
  
- lstrip() : 删除字符串左侧空白字符

  1. 快速体验

      ```
      mystr = "   hello world and itcast and itheima and Python   "
      
      new_str = mystr.lstrip()
      # 结果:hello world and itcast and itheima and Python   
      print(new_str)
      ```

      

- rstrip() : 删除字符串右侧空白字符

  1. 快速体验

      ```
      mystr = "   hello world and itcast and itheima and Python   "
      
      new_str2 = mystr.rstrip()
      # 结果:   hello world and itcast and itheima and Python
      print(new_str2)
      ```

  

- strip() : 删除字符串两侧空白字符

  1. 快速体验

      ```
      mystr = "   hello world and itcast and itheima and Python   "
      
      new_str3 = mystr.strip()
      # 结果:hello world and itcast and itheima and Python
      print(new_str3)
      ```

- ljust() :  返回一个原字符串左对齐,  并使用指定字符( 默认空格 ) 填充至对应长度的新字符串.

  1. 语法:

      ```
      字符串序列.ljust(长度, 填充字符)
      ```

      

  2. 输出效果

      ```
      mystr = 'hello'
      
      # 结果:  hello.....
      new_str1 = mystr.ljust(10, '.')
      print(new_str1)
      ```

      

- rjust() :  返回一个原字符串右对齐,  并使用指定字符( 默认空格 ) 填充至对应长度的新字符串,  语法和 ljust() 相同.

  1. 输出效果

      ```
      mystr = 'hello'
      
      # 结果:  .....hello
      new_str2 = mystr.rjust(10, '.')
      print(new_str2)
      ```

      

- center() :  返回一个原字符串居中对齐,  并使用指定字符( 默认空格 ) 填充至对应长度的新字符串,  语法和 ljust() 相同.

    1. 输出效果

        ```
        mystr = 'hello'
        
        # 结果:  ..hello...
        new_str3 = mystr.center(10, '.')
        print(new_str3)
        ```

        





















##### 4.3  判断

所谓判断即是判断真假,  返回的结果是布尔型数据类型:  True 或 False.

- ==startswith()== : 检查字符串是否以指定子串开头,  是则返回 True,  否则返回 False.  如果设置开始和结束位置下标,  则在指定范围内检查.

    1. 语法:

        ```
        字符串序列.startswith(子串, 开始位置下标, 结束位置下标)
        ```

        

    2. 快速体验

        ```
        mystr = "hello world and itcast and itheima and Python"
        
        # 1. startswith() -- 判断字符串是否以某个子串开头
        print(mystr.startswith('hello'))
        print(mystr.startswith('hel'))
        print(mystr.startswith('hels'))
        ```

    

- ==endswith()== :  检查字符串是否以指定子串开头,  是则返回 True,  否则返回 False.  如果设置开始和结束位置下标,  则在指定范围内检查.

    1. 语法:

        ```
        字符串序列.endswith(子串, 开始位置下标, 结束位置下标)
        ```

        

    2. 快速体验

        ```
        mystr = "hello world and itcast and itheima and Python"
        
        # 2. endswith() -- 判断字符串是否以某个子串结尾
        print(mystr.endswith('Python'))
        print(mystr.endswith('Pythons'))
        ```

    

- ==isalpha()== :  如果字符串至少有一个字符并且所有字符都是字母,  则返回 True,  否则返回 False.

    ```
    mystr1 = 'hello'
    mystr2 = 'hello12345'
    
    # 结果： True
    print（mystr1.isalpha())
    
    # 结果：False
    print(mystr2.isalpha())
    ```

    

- ==isdigit()== :  如果字符串只包含数字则返回 True,  否则返回 False.

    ```
    mystr1 = 'aaa12345'
    mystr2 = '12345'
    
    # 结果：False
    print(mystr1.isdigit())
    
    # 结果：False
    print(mystr2.isdigit())
    ```

    

- ==isalnum()== : 如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True，  否则返回False。

    ```
    mystr1 = 'aaa12345'
    mystr2 = '12345-'
    
    # 结果：True
    print(mystr1.isalnum())
    
    # 结果：False
    print(mystr2.isalnum())
    ```

    

- ==isspace()== : 如果字符串中只包含空白，则返回True，否则返回False。

    ```
    mystr1 = '1 2 3 4 5'
    mystr2 = '     '
    
    # 结果：False
    print(mystr1.isspace())
    
    # 结果：True
    print(mystr2.isspace())
    ```



### 五.  总结

- 下标

  - 计算机为序列中每个元素分配的从0开始的编号

- 切片

  ```
  序列名[开始位置下标：结束位置下标：步长]
  ```

  

- 常用操作方法

  - find()
  - index()
  - 







## 课程:  列表

目标

- 列表的应用场景
- 列表的格式
- 列表的常用操作
- 列表的循环遍历
- 列表的嵌套使用



### 一.  列表的应用场景

思考:  有一个人的姓名( Tom )怎么书写存储程序?

答:  变量

思考:  如果一个班级100位学生,  每个人的姓名都要存储,  应该如何书写程序?  声明100个变量吗?

答:  列表即可,  列表一次性可以存储多个数据.



### 二.  列表的格式

```
[数据1,数据2,数据3,数据4……]
```

列表可以一次性存储多个数据,  且可以为不同的数据类型



### 三.  列表的常用操作

列表的作用是一次性存储多个数据，程序员可以对这些数据进行的操作有：增、删、改、查。

#### 3.1  查找

##### 3.1.1  下标

```
name_list = ["Tom", "Lily", "Rose"]

print(name_list)

print(name_list[0])		# Tom
print(name_list[1])		# Lily
print(name_list[2])		# Rose
```



##### 3.1.2  函数

- ==index()== :  返回指定数据所在位置下标

    1. 语法

        ```
        列表序列.index( 数据,  开始位置下标,  结束位置下标)
        ```

        

    2. 快速体验

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        print(name_list.index("Tom"))
        print(name_list.index("Toms"))
        ```

        注意:  如果查找的数据不存在则报错

        

- ==count()== :  统计指定数据在当前列表中出现的次数

    1. 语法:

    2. 快速体验

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        print(name_list.count("Tom"))
        print(name_list.count("Toms"))  		# 没有即返回 0
        ```

        

- ==len()== :  访问列表长度,  即列表中数据的个数

    1. 语法:

    2. 快速体验

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        print(len(name_list)) 			# 3
        ```

        

##### 3.1.3  判断是否存在

- ==in== : 判断指定数据在某个列表序列中是否存在,  如果存在返回 True,  不存在则返回 False.

    1.  快速体验

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        # 1. in
        print("Lily" in name_list)
        print("Lilys" in name_list)
        ```

        

- ==not in== : 判断指定数据不在某个列表序列中,  如果不在返回 True,  存在则返回 False

    1. 快速体验

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        # 2.not in
        print("tom" not in name_list)
        print("Tom" not in name_list)
        ```

        

- 体验案例:

    需求:  查找用户输入的名字是否已经存在

    ```
    name_list = ["Tom", "Lily", "Rose"]
    
    name = input("请输入您的名字: ")
    print(f'您输入的名字为:{name}')
    
    if name in name_list:
        # 提示用户名已经存在
        print("The name you input has exists !")
    else:
        # 提示可以注册
        print("input successful!")
    ```

    

#### 3.2  增加

作用:  增加指定数据到列表中

- ==append()== : 列表结尾追加数据

    1. 语法: 

        ```
        列表序列.append( 数据 )
        ```

        

    2. 体验

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        name_list.append("xiaoming")
        
        print(name_list)
        ```

        列表追加数据的时候,直接在圆列表里面追加了数据,  即修改了原列表,   故列表为可变类型数据

        

    3. 注意点

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        name_list.append([11, 22])
        
        print(name_list)
        ```

​			如果 append() 追加的数据是一个序列,  则追加整个序列到列表





- ==extend()== :  列表结尾追加数据,  如果数据是一个序列,  则将这个序列的数据逐一添加到列表中.

    1. 语法:

        ```
        列表序列.entend( 数据 )
        ```

        

    2. 快速体验

        2.1 单个数据

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        name_list.extend("xiaoming")
        
        # 结果:  ['Tom', 'Lily', 'Rose', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g']
        print(name_list)
        
        ```

        

        2.2 序列数据

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        name_list.extend(["xiaoming", "xiaohong"])
        
        # 结果:  ['Tom', 'Lily', 'Rose', 'xiaoming', 'xiaohong']
        print(name_list)
        
        ```

        

- ==insert()== :  指定位置新增数据

    1. 语法:

        ```
        列表序列.insert( 位置下标,  数据 )
        ```

    2. 快速体验

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        # name_list.insert(下标, 数据)
        name_list.insert(1, "Lily")
        
        # 结果 : ['Tom', 'Lily', 'Lily', 'Rose']
        print(name_list)
        
        ```

#### 3.3  删除

- ==del==

    1. 语法:

        ```
        del 目标
        或  del ( 目标 )
        ```

        

    2. 快速体验

        2.1 删除列表

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        # del name_list
        # del(name_list)
        
        print(name_list)
        ```

        

        

        2.2 删除指定数据

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        del name_list[0]
        print(name_list)
        ```

        

- ==pop()== : 删除指定下标的数据( 默认为最后一个 ), 并返回该数据

    1. 语法

        ```
        列表序列.pop( 下标 )
        ```

        

    2. 快速体验

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        del_name = name_list.pop()
        del_name = name_list.pop(1)
        
        # 结果: Rose
        print(del_name)
        
        # 结果 : ['Tom', 'Lily']
        print(name_list)
        ```

    

- ==remove()== : 移除列表中某个数据的 <u>第一个</u> 匹配项,  即如果有两个 “Rose” ,  则只删除第一个.

    1. 语法:

        ```
        列表序列.remove( 数据 )
        ```

        

    2. 快速体验

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        name_list.remove("Lily")
        
        # 结果: ["Tom",  "Rose"]
        print(name_list)
        
        ```

        

- ==clear()== : 清空列表

    1. 快速体验

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        name_list.clear()
        
        # 结果: [ ]
        print(name_list)
        
        ```

#### 3.4  修改

- ==修改指定下标数据==

    1. 语法:

        ```
        name_list = ["Tom", "Lily", "Rose"]
        
        name_list[0] = "aaa"
        
        # 结果 : ["aaa", "Lily", "Rose"]
        print(name_list)
        
        ```

        

- ==逆置 : reverse()==

    1. 快速体验

        ```
        list1 = [1, 3, 2, 5, 4, 6]
        
        list1.reverse()
        
        # 结果 : [6, 4, 5, 2, 3, 1]
        print(list1)
        ```

        

- ==排序 : sort()==

    1. 语法:

        ```
        列表序列.sort( key=None,  reverse=False )
        ```

        注意: reverse表示排序规则, reverse = True 降序, reverse = False 升序 ( 默认 )

        

    2. 快速体验

        ```
        list1 = [1, 3, 2, 5, 4, 6]
        
        list1.sort()
        
        # 结果 : [1, 2, 3, 4, 5, 6]
        print(list1)
        ```



#### 3.5  复制

函数 : copy()

```
name_list = ["Tom", "Lily", "Rose"]


name_list2 = name_list.copy()

# 结果: ['Tom', 'Lily', 'Rose']
print(name_list)
print(name_list2)

```

```
#   工作中因为数据来之不易, 常常先将原始数据复制一份, 一份作保留, 另一份进行修改操作
```



### 四.  列表的循环遍历

需求: 依次打印列表中的各个数据

#### 4.1  while

- 代码

    ```
    name_list = ["Tom", "Lily", "Rose"]
    
    i = 0
    while i < len(name_list):		# 此处的 len 取得 3
        print(name_list[i])
        i += 1
        
    print("遍历结束")
    ```

    

- 执行结果

    ![](/home/ghr/图片/py教程/列表的遍历循环之while.png)

    

#### 4.2  for

- 代码

    ```
    name_list = ["Tom", "Lily", "Rose"]
    
    for i in name_list:
        print(i)
    ```

    

- 执行结果

    ![](/home/ghr/图片/py教程/列表的循环遍历之for.png)



#### 4.3  总结

由代码可看出,  在遍历序列中的数据时,  for 循环比 while 循环使用的代码少的多,  所以优先考虑使用 for 循环来遍历裂变中的数据.



### 五.  列表嵌套

所谓列表嵌套指的就是一个列表里面包含了其他的子列表.

应用场景:  要存储班级一,二,三三个班级里的学生姓名,  且每个班级的学生姓名在一个列表.

```
name_list = [["小明", "小红", "小绿"], ["Tom", "Lily", "Rose"], ["张三", "李四", "王五"]]

```

思考:  如何查找到数据 “ 李四 ”?



```
name_list = [["小明", "小红", "小绿"], ["Tom", "Lily", "Rose"], ["张三", "李四", "王五"]]

#  第一步:  按下标查找到 李四 所在的列表
print(name_list[2])

#  第二步 : 从 李四 所在的列表里面,  再按下标找到数据 李四
print(name_list[2][1])
```

 

### 六.  综合应用 – 随机分配办公室

需求:  有三个办公室,  8位老师,  8位老师随机分配到3个办公室

```

```



### 七.  总结

- 列表的格式

    ```
    [ 数据1, 数据2, 数据3]
    ```

    

- 常用操作方法

    - index( )

    - len( )

    - append( )

    - pop( )

    - remove( )

        

- 列表嵌套

    ```
    name_list = [["小明", "小红", "小绿"], ["Tom", "Lily", "Rose"], ["张三", "李四", "王五"]]
    
    print(name_list[2][1])    # 李四
    ```

    

