## 一. 进程

#### 进程的概念

```python
python中的多线程其实并不是真正的多线程，如果想要充分地使用多核CPU的资源，在python中大部分情况需要使用多进程。

进程的概念：
	 进程是程序的一次执行过程, 正在进行的一个过程或者说一个任务，而负责执行任务的则是CPU.
	
进程的生命周期：
	当操作系统要完成某个任务时，它会创建一个进程。当进程完成任务之后，系统就会撤销这个进程，收回它所占用的资源。从创建到撤销的时间段就是进程的生命期

进程之间存在并发性：
	在一个系统中，同时会存在多个进程。他们轮流占用CPU和各种资源

并行与并发的区别：
	无论是并行还是并发,在用户看来都是同时运行的，不管是进程还是线程，都只是一个任务而已， 
真正干活的是CPU，CPU来做这些任务，而一个cpu（单核）同一时刻只能执行一个任务。 

	并行：多个任务同时运行，只有具备多个cpu才能实现并行，含有几个cpu，也就意味着在同一时刻可以执行几个任务。 
	并发：是伪并行，即看起来是同时运行的，实际上是单个CPU在多道程序之间来回的进行切换。

同步与异步的概念：
	同步就是指一个进程在执行某个请求的时候，若该请求需要一段时间才能返回信息，那么这个进程将会一直等待下去，直到收到返回信息才继续执行下去。 
	异步是指进程不需要一直等下去，而是继续执行下面的操作，不管其他进程的状态。当有消息返回时系统会通知进行处理，这样可以提高执行的效率。 
	比如：打电话的过程就是同步通信，发短信时就是异步通信。

多线程和多进程的关系：
	对于计算密集型应用，应该使用多进程，因为可以使用多个CPU; 缺点是占用资源多。
	对于IO密集型应用，应该使用多线程。线程的创建比进程的创建开销小的多。

```

#### 创建进程

##### 使用multiprocessing.Process

```python
import multiprocessing
import time

def func(arg):
    pname = multiprocessing.current_process().name
    pid = multiprocessing.current_process().pid
    print("当前进程ID=%d,name=%s" % (pid, pname))

    for i in range(5):
        print(arg)
        time.sleep(1)

if __name__ == "__main__":
    p = multiprocessing.Process(target=func, args=("hello",))
    # p.daemon = True  # 设为【守护进程】（随主进程的结束而结束）
    p.start()

    while True:
        print("子进程是否活着？", p.is_alive())
        time.sleep(1)
    print("main over")

```

##### 通过继承Process实现自定义进程

```python
import multiprocessing
import os

# 通过继承Process实现自定义进程
class MyProcess(multiprocessing.Process):
    def __init__(self, name, url):
        super().__init__()
        self.name = name
        self.url = url  # 自定义属性

    # 重写run
    def run(self):
        pid = os.getpid()
        ppid = os.getppid()
        pname = multiprocessing.current_process().name
        print("当前进程name：", pname)
        print("当前进程id：", pid)
        print("当前进程的父进程id：", ppid)

if __name__ == '__main__':

    # 创建3个进程
    MyProcess("小分队1", "").start()
    MyProcess("小分队2", "").start()
    MyProcess("小分队3", "").start()
    print("主进程ID：", multiprocessing.current_process().pid)

    # CPU核数
    coreCount = multiprocessing.cpu_count()
    print("我的CPU是%d核的" % coreCount)

    # 获取当前活动的进程列表
    print(multiprocessing.active_children())
```

##### 同步异步和进程锁

```python
import multiprocessing
import random
import time

def fn():
    name = multiprocessing.current_process().name
    print("开始执行进程：", name)
    time.sleep(random.randint(1, 4))
    print("执行结束：", name)

# 多进程
# 异步执行进程
def processAsync():
    p1 = multiprocessing.Process(target=fn, name="小分队1")
    p2 = multiprocessing.Process(target=fn, name="小分队2")
    p1.start()
    p2.start()

# 同步执行
def processSync():
    p1 = multiprocessing.Process(target=fn, name="小分队1")
    p2 = multiprocessing.Process(target=fn, name="小分队2")
    p1.start()
    p1.join()
    p2.start()
    p2.join()

# 加锁
def processLock():
    # 进程锁
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=fn2, name="小分队1", args=(lock,))
    p2 = multiprocessing.Process(target=fn2, name="小分队2", args=(lock,))
    p1.start()
    p2.start()

def fn2(lock):
    name = multiprocessing.current_process().name
    print("开始执行进程：", name)

    # 加锁
    # 方式一
    # if lock.acquire():
    #     print("正在工作...")
    #     time.sleep(random.randint(1, 4))
    #     lock.release()

    # 方式二
    with lock:
        print("%s:正在工作..." % name)
        time.sleep(random.randint(1, 4))

    print("%s:执行结束："% name)


if __name__ == '__main__':
    # processAsync() # 异步执行
    # processSync()  # 同步执行
    processLock()  # 加进程锁

```

##### 使用Semaphore控制进程的最大并发

```python
import multiprocessing
import time

def fn(sem):
    with sem:
        name = multiprocessing.current_process().name
        print("子线程开始：", name)
        time.sleep(3)
        print("子线程结束：", name)

if __name__ == '__main__':
    sem = multiprocessing.Semaphore(3)
    for i in range(8):
        multiprocessing.Process(target=fn, name="小分队%d"%i, args=(sem, )).start()

```



## 二. 高阶函数

sorted(key=lambda x:x['age'])

reversed()

#### 1.map()

> 代码演示：
>
> ```python
> """
> map(function,iterable)
> function:函数
> iterable：可迭代对象
> 作用：将传入的函数依次作用于可迭代对象中的每一个元素，并把结果【Iterator】返回
> """
> #需求1：给一个已知列表中的元素求平方
> def square(x):
>     return x ** 2
> list1 = [1,2,3,4,5]
> result1 = map(square,list1)
> #注意:map是一个类，表示一种数据类型，集合或者序列，使用类似于list，tuple，set
> print(result1)   #<map object at 0x000001EE25431DA0>
> print(type(result1))   #<class 'map'>
> print(list(result1))  #[1, 4, 9, 16, 25]
>
> result2 = map(lambda x:x ** 2,list1)
> print(list(result2))
>
> #str = 10
>
> #需求2：将整型元素的列表转换为字符串元素的列表
> #举例：[1,2,3,4]------>["1","2","3","4"]
> #str(1) ---- >字符串1
> #注意：在使用系统函数之前，最好不要出现同名的变量
> result3 = map(str,[1,2,3,4])
> print(list(result3))
>
>
> #需求3：已知两个整型列表，将两个列表中相同位置的元素相加，得到一个新的列表
> def add(x,y):
>     return  x  + y
> l1 = [1,2,3,4,5]
> l2 = [6,7,8,9,10]
>
> result4 = map(add,l1,l2)
> print(list(result4))
> ```

#### 2.reduce()

> 代码演示：
>
> ```python
> from  functools  import  reduce
>
> """
> reduce(function,Iterable)  :通过函数对参数列表中的元素进行累积
> function:函数
> Iterable：可迭代对象，一般使用列表
> 工作原理：用传给reduce的function先作用于list中第一个和第二个元素，用得到的结果和list中第三个元素计算。。。
> reduce(add,[a,b,c,d])
> add(add(add(a,b),c),d)---->递归
> """
>
> #需求1;求一个已知列表中元素的和
> list1 = [1,2,3,4,5]
> def add(x,y):
>     return x + y
> result1 = reduce(add,list1)
> print(result1)
>
> result2 = reduce(lambda x,y:x + y,list1)
> print(result2)
>
> #需求2：将列表[1,3,5,7,9]变换成整数13579
> """
> 分析：
> 13 = 1 * 10 + 3
> 135 = 13 * 10 + 5
> 1357 = 135 * 10 + 7
> 13579 = 1357 * 10 + 9
> """
> list2 = [1,3,5,7,9]
> def fn(x,y):
>     return x * 10 + y
>
> result3 = reduce(fn,list2)
> print(result3)
>
> #需求3：
> #结合map函数，实现一个将str转换为int的函数   int()
>
> #思路：传进来一个字符串，返回一个对应的整数
> def strToInt(s):
>     digits = {"0":0,"1":1,"2":2,"3":3,"4":4}
>     return digits[s]
>
> #"23401"------>23401
> r0 = map(strToInt,"23401")
> print(list(r0))   #[2, 3, 4, 0, 1]
>
> r1 = reduce(fn,map(strToInt,"23401"))
> print(r1)   #23401
> print(type(r1))   #<class 'int'>
> ```

#### 3.filter()

> 代码演示：
>
> ```python
> """
> filter(function,序列)
> 作用：通过指定的条件过滤列表中的元素
> 工作原理：将传入的函数依次作用于列表中的每一个元素，根据返回的是True还是False决定元素是否需要保留
> """
>
> #需求1：将列表中的偶数筛选出来
> list1 = [1,2,3,4,5,6,7,8,9]
> #作用：定义筛选的规则
> def func(num):
>     if num % 2 == 0:
>         return  True
>     return  False
>
> result1  = filter(func,list1)
> print(result1)
> print(list(result1))  #[2, 4, 6, 8]
> ```

#### 4.sorted()

> 代码演示：
>
> ```python
> #1.普通排序
> #默认为升序排序，得到了的一个新的列表
> list1 = [4,5,23,3,5,7]
> result1 = sorted(list1)
> print(list1)
> print(result1)  #r[3, 4, 5, 5, 7, 23]
>
> #2.按照绝对值进行排序
> #默认为升序排序，排序的依据是所有元素的绝对值的大小
> list2 = [4,5,-23,3,-5,7]
> result2 = sorted(list2,key=abs)
> print(result2)  #[3, 4, 5, -5, 7, -23]
>
> #3.降序升序
> list3 = [4,5,23,3,5,7]
> result3 = sorted(list3,reverse=True)
> print(result3)
>
> #4.字符也可以实现排序
> list4 = ["f","a","k","z"]
> result4 = sorted(list4)
> print(result4)
>
> #5.自定义排序规则
> #默认为升序排序
> def myFunc(str):
>     return len(str)
> list5 = ["gsg","a","34535","efgg","562875678257fhjawhgj"]
> result5 = sorted(list5,key=myFunc)
> print(result5)
> ```







