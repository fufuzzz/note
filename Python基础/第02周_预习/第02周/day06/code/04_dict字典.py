# 字典: dict dictionary
#   1. 字典中的元素是一个键值对: key-value, {"name: "小红"}
#   2. key的特点:
#       a. 唯一
#       b.不可变类型
#       c.无序

# 基本操作
# 1.创建字典
d = {'name': '鹿晗', 'age': 31}
# d = {1: 2, 2: 3, True: 4, (): 5, 1: 999}
print(d, type(d))

# 2. 查找元素: 通过key来取值,不能用索引
print(d['name'])
# print(d['sex'])  # 报错,不存在的key无法取到

print(d.get('name'))
print(d.get('sex'))  # None,但不会报错
print(d.get('sex', '男'))  # 男, 默认值
print(d.get('name', '张三'))  # 鹿晗

#  如果key是变量,则不能在key的两边加引号
key = 'name'
print(d[key])
# print(d['key'])  # 不行


# 3.长度
print(len(d))  # 2

# 4.遍历
d = {'name': '鹿晗', 'age': 31}

for k in d:
    print(k, d[k])  # key

for v in d.values():
    print(v)  # value

# for k in d.keys():
#     print(k)  # key

for k, v in d.items():
    print(k, v)  # key,value

# print(d.keys(), type(d.keys()))
# print(d.values())
print(list(d.keys()))  # ['name', 'age']
print(list(d.values()))  # ['鹿晗', '31']

# 切片(没有)
# 重复(没有)
# 5.合并
d = {'name': '鹿晗', 'age': 31}
d1 = {1: 2}
d2 = {2: 3}
d1.update(d2)
print(d1, d2)  # {1: 2, 2: 3} {2: 3}

# 6.判断成员
d = {'name': '鹿晗', 'age': 31}
print("name" in d)  # True

# 其他功能
# 增删改查

d = {'name': '鹿晗', 'age': 31}

# 增: key不存在就是增加
d['sex'] = '男'
print(d)

# 改: key存在则会修改
d['name'] = '蔡徐坤'
print(d)

# 查
print(d['name'])
print(d.get('name'))

# 删
d = {'name': '鹿晗', 'age': 31}
# d.pop('age')  # 弹出指定key的元素
# d.clear()  # 清空字典
# d.popitem()  # 删除最后一项,随机删除一项
# del d ['age']
print(d)

# zip()
# 创建字典
d = dict(name="张三", age=33)
print(d)  # {'name': '张三', 'age': 33}

d = dict(zip(['name', 'age'], ['特朗普', 74]))
d = dict(zip('abc', '123'))
print(d)

d = dict(list(zip(['name', 'age'], ['特朗普', 74])))

d = dict({'a': 1})
d = dict([(1,'a'),(2,'b')])  # 可迭代对象
d = dict(([1,'a'],[2,'b']))
d = dict((['name', 'age'], ['特朗普', 74]))
print(d)

