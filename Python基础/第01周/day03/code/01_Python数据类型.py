# Python 数据类型
#   Number数值类型: int整数,float浮点数/小数,complex复数
#   String字符串类型: str
#   Boolean布尔类型: bool,有2个值:True,False
#   NoneType空值类型: NoneType, 有1个值: None
#
#   list: 列表类型/数组
#   tuple: 元组类型/不可改变的列表
#   dict: 字典类型
#   set: 集合类型(了解)
#   bytes: 字节/二进制类型

#   int
a = 10  # 10 <class 'int'>
a = 10.2  # 10.2 <class 'float'>
a = '鹿晗'  # 鹿晗 <class 'str'>
a = False  # False <class 'bool'>
a = None  # None <class 'NoneType'>

a = [1, 2, 3]  # [1, 2, 3] <class 'list'>
a = (1, 2, 3)  # (1, 2, 3) <class 'tuple'>
a = {1, 2, 3}  # {1, 2, 3} <class 'set'>
a = {'name': '鹿晗', 'movie': '上海堡垒', 'age': 31}  # {'name': '鹿晗', 'movie': '上海堡垒', 'age': 31} <class 'dict'>
a = b'hello'  # b'hello' <class 'bytes'>

print(a, type(a))

print(int(True))   # 1
print(int(False))  # 0
