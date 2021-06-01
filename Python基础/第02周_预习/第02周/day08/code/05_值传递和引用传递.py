# 基本类型/不可变类型:
#   int, float,str,tuple,bool,None
# 引用类型/不可变类型
#   list,dict,set


# 赋值
# 基本类型赋值: 不关联
a = 100
b = a
a = 200
print(a, b)  # 200 100

# 引用类型赋值: 关联
l1 = [1, 2, 3]
l2 = l1
l2[0] = 888
print(l1, l2)

#
x = 10
y = {'name': '郑爽', 'age': 28}


def fn(x, y1):
    x += 1
    y['age'] += 1
    print(x, y)


fn(x, y)

print('after:', x, y)
