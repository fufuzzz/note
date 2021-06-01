## Day04-分支和循环

### 一、分支【重点掌握】

#### 1.代码结构

> 顺序结构：代码从上往下依次执行
>
> 分支结构：根据不同的条件，执行不同的语句
>
> 循环结构: 根据指定的条件，重复执行某段代码

#### 2.分支结构-if语句 

##### 2.1简单if语句【单分支】

> 语法：
>
> if 表达式：
>
> ​	执行语句
>
> 说明;要么执行，要么不执行，当表达式成立的之后，则执行语句；如果表达式不成立，则直接跳过整个if语句继续执行后面的代码
>
> 注意：表达式为真才执行语句
>
> ​           假：0    0.0   False   “”   None【空值】
>
> ​	一般情况下，表达式使用都是比较运算符
>
> 代码演示：
>
> ```Python
> #单分支
> num1 = 50
> num2 = 60
> 
> #需求：当num1 == num2,则给num1重新赋值为100
> 
> #在pYthon中，通过缩进来区分代码块
> if num1 != num2:
>  	num1 = 100
> 
> print(num1)
> 
> 
> #练习：从控制台输入一个数，判断这个数是否是偶数
> num = int(input())
> if num % 2 == 0:
>  	print(num,"是一个偶数")
> 
> print(num,"不是一个偶数")
> ```

##### 2.2if-else语句【双分支】

> 语法：
>
> if 表达式：
>
> ​	执行语句1
>
> else:
>
> ​	执行语句2
>
> 说明：如果表达式成立，则执行语句1；如果不成立，则执行语句2
>
> 代码演示：
>
> ```Python
> #双分支
> #  从控制台输入一个数，判断这个数是否是偶数
> num = int(input())
> 
> if num % 2 == 0:
>  	print(num,"是一个偶数")
> else:
>  	print(num,"不是一个偶数")
> 
> 
> #练习：从控制台输入一个数字，根据数字打印年龄段
> age = int(input())
> if age >= 18:
>  	print("成年人")
> else:
>  	print("未成年人")
> ```

##### 2.3if-elif-else语句【多分支】

> 语法：
>
> if 表达式1：
>
> ​	执行语句1
>
> elif 表达式2：
>
> ​	执行语句2
>
> elif 表达式3：
>
> ​	执行语句3
>
> 。。。。。
>
> else:
>
> ​	执行语句n
>
> 说明：实现了多选一的操作，会根据不同的条件从上往下来进行匹配，如果匹配上了，则执行对应的语句，然后直接结束整个if-elif语句，但是，如果所有的条件都不成立的话，则执行else后面的语句
>
> 注意：不管if-elif-else有多少个分支，都只会执行其中的一个分支
>
> 代码演示：
>
> ```Python
> #多分支
> #需求：从控制台输入一个数字，根据数字打印年龄段
> age = int(input())
> if age < 0:
>  	print("输入有误")
> elif age <= 3:
>  	print("婴儿")
> elif age <= 6:
>  	print("儿童")
> elif age <= 12:
>  	print("青少年")
> elif age <= 18:
>  	print("青年")
> else:
>  	print("hello")
> ```

> ```Python
> #练习：根据控制台输入的成绩，输出对应的等级
> """
> 90以上：优秀
> 80~90：良好
> 70~80：还行
> 70以下：加油吧，少年
> """
> score = int(input("请输入学生的成绩："))
> if score >= 90:
>  	print("优秀")
> elif score >= 80:
>  	print("良好")
> elif score >= 70:
>  	print("还行")
> else:
>  	print("")
> ```

##### 2.4嵌套if语句

> 语法：
>
> if 表达式1：
>
> ​	执行语句1
>
> ​	if 表达式2：
>
> ​		执行语句2
>
> 说明：if语句的嵌套，可以在单分支，双分支，多分支之间进行任意组合
>
> 代码演示：
>
> ```Python
> score = int(input("请输入学生的成绩："))
> if score < 0 or score > 100:
>  	print("输入有误")
> else:
>  	if score >= 90:
>      	print("优秀")
>  	elif score >= 80:
>      	print("良好")
>  	elif score >= 70:
>      	print("还行")
>  	else:
>      	print("")
> 
> age = int(input("请输入年龄："))
> looks = input("请输入您的相貌：")
> 
> if age >= 18:
> 	if looks == "美女":
>      		print("要微信")
>  	else:
>      		print("略过")
> ```
>
> 注意：从语法角度来说，嵌套的层数没有任何的限制，但是，为了代码的可读性和可维护性，嵌套层数不要超过3层



### 二、循环【掌握】

#### while循环+for循环

#### 1.用法

> 语法：
>
> 初始化表达式
>
> while  条件表达式：
>
> ​	循环体
>
> ​	循环之后操作表达式
>
> 
>
> for 变量名 in 序列：
>
> ​	循环体
>

#### 2.range

> range([start,]end[,step])      注：[]表示start和step可写可不写
>
> start:开始数字
>
> end；结束数字
>
> step；步长
>
> start默认为0，step默认为1 
>
> 功能：生成具有一定规律的序列
>
> 代码演示：
>
> ```Python
> #range()
> """
> range([start,]end[,step])
> l例如：
> range(100)    可以生成一个0~99的整数序列【不包含100】
> range（1,100）  可以生成一个1~99的整数序列
> range(1,100,2)  可以生成一个1~99之间的奇数序列
> """
>
> #需求1：计算1~100之间所有整数的和
> num1 = 1
> sum1 = 0
> while num1 <= 100:
>     	sum1 += num1
>     	num1 += 1
>
> sum11 = 0
> #借助于range生成一个1~100之间所有整数的序列，然后使用for循环进行遍历这个序列
> for x in range(1,101):
>     	sum11 += x
>
> #需求2：计算1~100之间所有偶数的和
> num2 = 1
> sum2 = 0
> while num2 <= 100:
>     	if num2 % 2 == 0:
>         	sum2 += num2
>     	num2 += 1
>
> num2 = 0
> sum2 = 0
> while num2 <= 100:
>     	sum2 += num2
>     	num2 += 2
>
> sum22 = 0
> for y in range(0,101,2):
>     	sum22 += y
> ```



#### 4.嵌套循环

> 代码演示：
>
> ```Python
> #需求：打印九九乘法表
>
> #while实现
> line = 1
> while line <= 9:
>     	colum = 1
>     	while colum <= line:
>         	print("%dx%d=%d"%(colum,line,line*colum),end=" ")
>         	colum += 1
>     	print("")
>     	line += 1
>
>
> #for实现
> #外层循环：控制行
> for i in range(1,10):
>     	#内层循环：控制列
>     	for j in range(1,i + 1):
>         	print("%dx%d=%d"%(j,i,i*j),end=" ")
>     	print("")
> ```



### 三. break、continue和pass语句的使用

#### 1.break

> 作用:跳出循环【直接跳出整个循环，继续执行循环后面的代码】
>
> 代码演示：
>
> ```python
> #break的使用
> #1.while
> n = 0
> while n < 5:
>     	print("n = %d"%(n))
>     	#print("n =" ,n)
>     	#注意：if语句充当的是一个条件判断
>     	if n == 3:
>         	break
>     	n += 1
> print("over")
>
> #2.for
> for x in range(1,6):
>  	print("x = %d"%(x))
>     	if x == 3:
>         	break
>    #结论：不管是while语句还是for语句，break的作用结束整个循环
> 
>#3.特殊情况一
> #不管while中的条件是否满足，else分支都会被执行
> #思考问题：如果在while循环体中出现了break，else分支还会执行吗？-------不会
> m = 0
> while m < 3:
>  	print(m)
>     	if m == 1:
>         	break
>     	m += 1
>    else:
>  	print("else")
>    
>#4.特殊情况二
> #当break使用在嵌套循环中的时候，结束的是当前循环【就近原则】
> x = 0
> y = 0
> while x < 20:
>  	print("hello Python",x)
>     	x += 1
>     	while y < 5:
>         	print("hello Python~~~~",y)
>         	if y == 2:
>             	break
>         	y += 1
>     #break
>    
>#注意：break是一个关键字，使用的过程中，单独就可以成为一条语句，后面不能跟任何的变量或者语句
> ```

#### 2.continue

> 作用：跳出当前正在执行的循环，继续执行下一次循环
>
> 代码演示：
>
> ```python
> #continue的使用
>
> #1.for
> for i in range(10):
>     	print(i)
>     	if i == 3:
>         	continue
>     	print("*")
>
> for i in range(10):
>     	print(i)
>     	if i == 3:
>         	break
>     	print("*")
>
> #总结：continue只是结束当前正在执行的循环，而break表示直接结束整个循环
>
> # 2.while
> """
> num = 0
> while num < 10:
>     	print("num = %d"%(num))
>     	num += 1
>     	if num == 3:
>         	continue
> """
> num = 0
> while num < 10:
>     	if num == 3:
>         	num += 1
>         	continue
>     	print("num = %d" % (num))
>     	num += 1
> ```

#### 3.pass

> Python中的pass是一条空语句
>
> 作用：为了保持代码结构的完整性，pass不做任何操作，只是充当了一个占位语句，保证代码可以正常的运行起来
>
> 应用场景：if，while，for中使用，可以在代码块的部分不添加任何语句，代码正常运行
>
> 代码演示：
>
> ```python
> while True:
>     	pass
>
> print("over")
> ```

#### 4.练习

> 代码演示：

```python
#需求;判断一个数是否是素数【质数】
#方式一
num1 = int(input("请输入一个数："))
#思路：一个数能被其他数整除，将次数记录下来
#条件：在2~num1 - 1的范围内，找到一个数能将num1整除，count1 + 1
count1 = 0
for i in range(2,num1):
    #整除：求余【大数对小数求余】
    if num1 % i == 0:
        count1 += 1

if count1 == 0 and num1 != 1:
    print("是质数")
else:
    print("不是质数")

#方式二：
#思路：假设num2是质数，寻找不成立的条件【有数能被整除】将假设推翻掉
num2 = int(input("请输入一个数："))
#定义一个布尔类型的变量，用于记录这个数是不是一个质数
is_prime  = True
for j in range(2,num2):
    if num2 % j == 0:
        is_prime = False
        break

if is_prime == True and num2 != 1:
    print("是质数")
else:
    print("不是质数")
```

