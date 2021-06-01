## Day06-元组&字典&集合

### 一、tuple元组

#### 1.概述

> 和列表相似，本质上是一种有序的集合
>
> 元组和列表的不同之处：
>
> ​	a.列表:[ ]     元组：( )
>
> ​	b.列表中的元素可以进行增加和删除操作，但是，元组中的元素不能修改【元素：一旦被初始化，将不能发生改变】

#### 2.创建元组

> 创建列表:
>
> ​	创建空列表：list1 = [ ]
>
> ​	创建有元素的列表：list1 = [元素1，元素2，。。。。。]
>
> 创建元组
>
> ​	创建空元组：tuple1 = ( )
>
> ​	创建有元素的元组：tuple1 = (元素1，元素2，。。。。)
>
> 代码演示：
>
> ```Python
> #创建空元组：
> tuple1 = ()
> 
> #创建有元素的元组：
> tuple2 = (10,20,30)
> 
> #在元组中可以存储不同类型的数据
> tuple3 = ("hello",True,100)
> 
> #注意：创建只有一个元素的元组
> #按照下面的方式书写，表示定义了一个整型的变量，初始值为1
> tuple4 = (1)
> tuple4 = 1
> #为了消除歧义，修改如下：
> tuple4 = (1,)
> 
> num1 = 10
> num2 = (10)
> print(num1,num2)
> ```

#### 3.元组元素的访问

> 代码演示：
>
> ```Python
> #元组元素的访问
> #格式：元组名[索引],和列表完全相同
> tuple1 = (10,20,30,40,50)
> #1.获取元素值
> print(tuple1[2])
> #获取元组中的最后一个元素
> print(tuple1[4])
> #print(tuple1[5])  #IndexError: tuple index out of range  索引越界
> 
> #正数表示从前往后获取，负数表示从后往前获取
> print(tuple1[-1])
> print(tuple1[-2])
> print(tuple1[-5])
> # print(tuple1[-6])   #IndexError: tuple index out of range  索引越界
> 
> #2.修改元素值----->不能修改，本质原因不能修改元素的地址
> #和列表不同的地方：元组的元素值不能随意的更改
> #tuple1[1] = 100
> tuple2 = (1,35,54,[4,5,6])
> #获取元组中列表中的元素
> print(tuple2)   #(1, 35, 54, [4, 5, 6])
> tuple2[3][1] = 50
> print(tuple2)  #(1, 35, 54, [4, 50, 6])
> 
> #3.删除元组
> tuple3 = (53,6,7,76)
> del tuple3
> ```

#### 4.元组操作

> 代码演示：
>
> ```Python
> #1.元组组合
> #+
> tuple1 = (3,43,5,4)
> tuple2 = (3,5,45,4)
> print(tuple1 + tuple2)
> 
> #2.元组重复
> #*
> print(tuple1 * 3)
> 
> #注意：元组组合和元组重复得到的是一个新的元组，原来的元组并没有发生任何改变
> 
> #3.判断元素是否在元组中
> #成员运算符
> #in    not in
> print(100 in tuple1)
> print(100 not in  tuple1)
> 
> #4.元组截取【切片】
> tuple3 = (1,23,43,54,54,656,57,6)
> print(tuple3[2:4])
> print(tuple3[2:])
> print(tuple3[:4])
> ```

#### 5.元组功能

> 代码演示：
>
> ```Python
> #1.获取元组的元素个数
> tuple1 = (54,3,5,46,56)
> print(len(tuple1))
> 
> #2.获取元组中元素的最大值和最小值
> print(max(tuple1))
> print(min(tuple1))
> 
> 
> #3.元组和列表之间的相互转换:取长补短
> #3.1   元组-----》列表
> #list()
> list1 = list(tuple1)    #int()   float()
> print(list1)
> 
> #3.2  列表------》元组
> #tuple()
> list2 = [34,5,46,4]
> tuple2 = tuple(list2)
> print(tuple2)
> 
> #4.遍历元组
> #4.1直接遍历元素
> for n in tuple1:
>  	print(element)
> 
> #4.2遍历索引
> for index in range(len(tuple1)):
>  	print(tuple1[index])
> 
> #4.3同时遍历索引和元素
> for i,num in enumerate(tuple1):
>  	print(i,num)
> ```

#### 6.二维元组

> 代码演示：
>
> ```Python
> #当做一维元组进行处理，实质：一维元组中的元素为一个一维元组
> tuple1 = ((2,43,5),(54,65,6),(5,54,54,54))
> print(tuple1[1][1])
> 
> #遍历二维列表或者二维元组的思路：嵌套循环
> #遍历外层元组
> for element in tuple1:
> 	#遍历内层元组
>  for num in elment:
>    print(num)
> ```



### 二、字典dict

#### 1.概念

> 列表和元组的使用缺点：当存储的数据要动态添加、删除的时候，我们一般使用列表，但是列表有时会遇到一些麻烦
>
> ```python
> # 定义一个列表保存，姓名、性别、职业
> nameList = ['尼古拉斯.赵四',  '铁憨憨'];
>
> # 当修改职业的时候，需要记忆元素的下标
> nameList[2] = '演员'  
>
> # 如果列表的顺序发生了变化，添加年龄
> nameList = ['尼古拉斯.赵四', 18, '男',  '铁匠']
>
> # 此时就需要记忆新的下标，才能完成名字的修改
> nameList[3] = 'xiaoxiaoWang'
> ```
>
> 解决方案：既能存储多个数据，还能在访问元素的很方便的定位到需要的元素，采用字典
>
> 语法： {键1: 值1, 键2: 值2, 键3: 值3, ..., 键n: 值n} 
>
> 说明：键值对: key-value
>
> - 字典和列表类似，都可以用来存储多个数据
> - 在列表中查找某个元素时，是根据下标进行的；字典中找某个元素时，是根据'名字'（就是冒号:前面的那个值，例如上面代码中的'name'、'id'、'sex'）
> - 字典中的每个元素都由2部分组成，键:值。例如 'name':'班长' ,'name'为键，'班长'为值
> - 键可以使用数字、布尔值、元组，字符串等不可变数据类型，但是一般习惯使用字符串，切记不能使用列表等可变数据类型
> - 每个字典里的key都是唯一的，如果出现了多个相同的key,后面的value会覆盖之前的value
>
> 习惯使用场景：
>
> - 列表更适合保存相似数据，比如多个商品、多个姓名、多个时间
> - 字典更适合保存不同数据，比如一个商品的不同信息、一个人的不同信息
>

#### 2.定义字典


```python
#语法：字典名 = {key1:value1,key2:value2.....}

#1.创建空字典
dict1 = {}
print(dict1,type(dict1))

#2.创建非空字典
#方式一
dict21 = {"name":"张三","age":18}
print(dict21)

#方式二
#dict(key=value),key是一个变量名，value是一个值
dict22 = dict(a="avvv",b="2353")
print(dict22)
dict22 = dict(a=200,b=33)
print(dict22)

#方式三
#dict()和zip(序列),zip表示映射
#dict(zip([key1,key2,key3....],[value1,value2,value3....]))
#注意：key的数量和value的数量可以不一致，以少的作为参考
z1 = zip([1,2],["a","b","c"])
dict23 = dict(z1)
print(dict23)

dict23 = dict(zip(("name","age"),("aaa",10)))
print(dict23)

dict23 = dict(zip("xyz","abc"))
print(dict23)

#方式四
# [(key1,value1), (key2,value2)...] => {key1:value1, key2:value2....}
dict24 = dict([("a",10),("b",20),("c",30)])
print(dict24)
```



### 三、set集合【了解】

#### 1.概述

> 和数学上的集合基本是一样的，
>
> 特点:不允许有重复元素，可以进行交集，并集，差集的运算
>
> 本质：无序，无重复元素的集合

#### 2.创建

> set(列表或者元组或者字典)
>
> 代码演示：
>
> ```Python
> #注意：set的创建需要借助于list和tuple
>
> #1.通过list创建set
> list1 = [432,5,5,46,65]
> s1 = set(list1)
> print(list1)
> print(s1)
>
> #注意1：set中会自动将重复元素过滤掉
>
> #2.通过tuple创建set
> tuple1 = (235,45,5,656,5)
> s2 = set(tuple1)
> print(tuple1)
> print(s2)
>
> #3.通过dict创建set
> dict1 = {1:"hello",2:"good"}
> s3 = set(dict1)
> print(dict1)   #{1: 'hello', 2: 'good'}
> print(s3)   #{1, 2}
>
> #注意2：set跟dict类似，都使用{}表示，但是与dict之间的区别在于：set中相当于只存储了一组key，没有value
> ```

#### 3.操作

##### 3.1添加

> 代码演示：
>
> ```Python
> #1.添加
> #add()   在set的末尾进行追加
> s1 = set([1,2,3,4,5])
> print(s1)
> s1.add(6)
> print(s1)
>
> #注意：如果元素已经存在，则添加失败
> s1.add(3)
> print(s1)
> #print(s1.add(3))
>
> #s1.add([7,8,9])   #TypeError: unhashable type: 'list'  list是可变的，set中的元素不能是list类型
> s1.add((7,8,9))
> #s1.add({1:"a"})  #TypeError: unhashable type: 'dict'  ，dict中的键值对可以改变，set中的元素不能是dict类型
> print(s1)
>
> #update()   插入【末尾添加】，打碎插入【直接将元组，列表中的元素添加到set中，将字符串中的字母作为小的字符串添加到set中】
> s2 = set([1,2,3,4,5])
> print(s2)
> s2.update([6,7,8])
> s2.update((9,10))
> s2.update("good")
> #注意：不能添加整型，因为整型不能使用for循环遍历
> #s2.update(11)   #TypeError: 'int' object is not iterable
> print(s2)
> ```

##### 3.2删除

> 代码演示：
>
> ```Python
> #2.删除
> #remove()
> s3 = set([1,2,3,4,5])
> print(s3)
> s3.remove(3)
> print(s3)
> ```

##### 3.3遍历

> 代码演示：
>
> ```Python
> #3.set的遍历
> s4 = set([1,2,3,4,5])
> for i in s4:
>     print(i)
>
> #注意：set是没有索引的，所以不能通过s4[2]获取元素，原因：set是无序的
> #print(s4[2])  #TypeError: 'set' object does not support indexing
>
> #注意：获取的是编号和元素值
> for i,num in enumerate(s4):
>     print(i,num)
> ```

##### 3.4交集和并集

> 代码演示：
>
> ```Python
> #4.交集和并集
> s4 = set([1,2,3])
> s5 = set([4,5,3])
>
> #交集：&【按位与】    and
> r1 = s4 & s5
> print(r1)
> print(type(r1))
>
> #并集:|【按位或】   or
> r2 = s4 | s5
> print(r2)
> ```


