# 二、
# # 说明：可以把这个字典看成数据表，id是自增id，name是省市名称，pid是父类
# # pid=0表示省，pid是一个非零值表示的是属于哪个父类，对应的是自增id
# # 比如   {'id': 15, 'name': '和平街', 'pid': 12} 这行数据，pid=12 表示 它的父级是 id=12的数据，就是武昌区，武昌区的pid=6，表示它的父级是id=6的数据，也就是武汉市，以此类推

area = [

    {'id': 1, 'name': '广东省', 'pid': 0},
    {'id': 2, 'name': '湖北省', 'pid': 0},
    {'id': 3, 'name': '湖南省', 'pid': 0},
    {'id': 4, 'name': '广州市', 'pid': 1},
    {'id': 5, 'name': '深圳市', 'pid': 1},
    {'id': 6, 'name': '武汉市', 'pid': 2},
    {'id': 7, 'name': '襄阳市', 'pid': 2},
    {'id': 8, 'name': '长沙市', 'pid': 3},
    {'id': 10, 'name': '天河区', 'pid': 4},
    {'id': 11, 'name': '罗湖区', 'pid': 5},
    {'id': 12, 'name': '武昌区', 'pid': 6},
    {'id': 13, 'name': '樊城区', 'pid': 7},
    {'id': 14, 'name': '芙蓉区', 'pid': 8},
    {'id': 15, 'name': '和平街', 'pid': 12},

]

# 1，写一个递归函数，给一个id，能够找到这个id对应的省的名字
# getName(15)  # 湖北省
def getName(id):
    for n in area:
        if n['id'] == id and n['pid'] != 0:
            # print(n['pid'])
            getName(n['pid'], area)
        elif n['id'] == id and n['pid'] == 0:
            # print('1')
            print(n['name'])
            return
    else:
        print('没有找到')


getName(17)
#
# 2, 写一个递归函数，输出如下形式的数据
def ergodic(count, id2=0):
    for n in area:
        if n['pid'] == id2:
            print('\t' * count, n['name'])
            ergodic(count+1, n['id'])
    else:
        return


ergodic(0)




# 广东省
# 广州市
# 天河区
# 深圳市
# 罗湖区
# 湖北省
# 武汉市
# 武昌区
# 和平街
# 襄阳市
# 樊城区
# 湖南省
# 长沙市
# 芙蓉区
