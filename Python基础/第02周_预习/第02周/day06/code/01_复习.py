''''''

'''
一.list列表
基本操作:
    1.创建列表:
        age = [1, 2, 3]
    2.索引:
        print(age[0])
        print(age[1])
        print(age[2])
        print(age[-1])  # 倒数第一个
    3.长度:
        print(len(ages))
    4.遍历:
        for n in ages:
            print(n)  # 元素
        for i in range(len(ages)):
            print(i, ages[i])  # 下标,元素
         for i, n in enumerate(ages):
            print(i, n)  # 下标,元素
    5.切片:
        ages[:]
        ages[2:]
        ages[:4]
        ages[2:4]
        ages[2:-1]
        ages[:-1]
    6.
    
    
    
    7.合并:
        [1, 2, 4] + [4, 5, 1]
    8.判断成员:
        if 3 in ages:
            print()
        not in
    9.删除:
        del ages
        del ages[0]
        del ages[2:4]

列表的功能: 
    增删改查:
        增:
            append(n): 追加一个元素
            insert(i, n): 在第i个下标的位置插入一个新元素n
            extend([]) : 在列表末尾追加另一个列表的元素
        删:
            n = pop(i): 弹出指定下标i的元素
            remove(n): 删除第一个元素n
             count(n): 统计n在列表中出现的次数
            clear(): 请空列表
            del 删除元素
        改:
            ages[0] = 99
        查:
            print(ages[0])
            
    其他功能:
        ages.index(n): 查找元素n在列表中第一次出现的下标,如果不存在,则报错
        ages.sort(): 按大小升序,会改变原列表
        sorted(ages): 升序,不会改变原列表
        ages.sort(reverse = True): 降序,会改变原列表
        ages.reverse(): 纯粹的倒序,会改变原列表 
        reversed(ages): 倒序,不会改变原列表
        print(list(ages.reverse()))
        
        age.copy(): 浅拷贝
        import copy
        copy.deepcopy(ages): 深拷贝
        

二.数学函数
    sum()
    max()
    min()
    round() : 四舍五入
    
    math.sqrt: 求开方
    math.pi
    math.ceil(): 向上取整
    math.floor(): 向下取整
    math.sin() : 正弦函数
    math.factorial():求阶层
    math.modf(22.3): 获取整数和小数,元组格式
'''
import copy

ages1 = [1, 2, 3]
ages2 = ages1.copy()
ages2[0] = 99
print(ages1, ages2)

ages1 = [1, 2, 3, [4, 5]]
ages2 = copy.deepcopy(ages1)
ages2[0] = 99
print(ages1, ages2)


