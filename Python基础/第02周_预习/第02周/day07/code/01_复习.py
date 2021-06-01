''''''

'''
1.随机数
import random
random.choice()
random.randint()
random.randrange()
random.random()
random.uniform(a, b): a + (b-a) * random.random()
random.shuffle()


2.元组
    1.创建元组
        t()
        t = (1,)
    2.索引
        t[0]
        t[-1]
    3.长度
        len(t)
    4.遍历
        for n in t:
            print(t)
        for i in range(len(t))
            print(i)
        for i , n in enumerrate(t):
            print(i)
    5.重复
        t *3
    6.切片
        t[3:5]            
        t[::-1]            
    7.合并
        (1,2) + (3,4)
    8.判断成员
        3 in t
    9.删除
        del t
    
    
    其他功能
        sorted()
        
        reversed()
        
        list()
        tuple()
        
        t = (1,2,[3,4)
        t[-1][0] = 99  #可以修改
        
        
3.字典
    key-value 键值对
    key特点:
        1. 唯一
        2. 无序
        3. 不可变类型
    
    1.创建字典
        d = {}
        d = {"name": "鹿晗", "age": 31}
        d = dict(name='蔡徐坤', age = 25}
        d = dict(zip['name','age'],['张三',19]))
    2.查询
        d['name']
        d.get
        
    3.长度
     len(d)
    4.遍历
        for k in d:
          print(k)    
        for n in d
        
        for v in d.values():
        
        for k v in d.items():
        
    5.成员
        if 'name' in d:
            print('name存在字典的key中')
            
    6.合并
        d1.update(d2)
    增,改: (有就改,没有就加上去)
        d['sex'] = '男'
        d['name'] = '李四'
    
    删:
        d.pop(key)
        d.popitem()
        d.clear()
        del d['name']
        

4.集合(了解)
    特点: 唯一,无序,不可变类型
    1.创建
        s = {1,2}
        s = set()
        s = set([1,2,3,4])
    2.长度
        len(s)
    3.遍历
        for n in s:
    4.去重:
        l = [1,2,3,2,2,2]
        print(list(set(l)))
        
    5.其他操作
        增: add(), update()
        删: pop(),remove(33),discard(33),clear()
        
        交集: s1 & s2
        并集: s1 | s2
        差集: s1 - s2
        对称差集: s1 ^ s2
        是否包含: s1 > s2
        是否被包含: s1 < s2
    
        
        
'''