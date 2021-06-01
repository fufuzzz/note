#
#
# class A:
#     def __init__(self, name):
#         self.name = name
#
#
# a = A('sss')
# print(a.name)
# a.age = 2
# print(a.age)
#
#
# d = dict(name="张三")
# print(d)
#
# s = 'abc123'
# # s_list = list(s)
# # s_list.reverse()
# z =''
# for i in range(len(s)-1, -1, -1):
#     z += s[i]
#
# print(z)
#
#
# str1 = "Nanjing University"
#
# str2 = str1[:7] + " Normal " + str1[-10:]
# print(str1[:7])
# print(str2)
#
# f1 = lambda x: (2 * x + 1)
# print(f1(5))
#
# import datetime
#
# d = datetime.datetime(year=2021, month=2, day=4, hour=21, minute=2, second=30)
# print(d)
#
# list0 = ['nice', '你好', '今天天气真好', 'beautiful', 'family', [27, 19, 33]]
# new_list = [n for n in list0 if isinstance(n, str)]
# print(new_list)


def myfind(string, substring):
    if substring not in string:
        return -1
    else:
        # 方法一 return string.index(substring)
        for i in range(len(string) - len(substring)):
            if string[i:i+(len(substring))] == substring:
                return i

print('i love you baby'[:4])
print(myfind('i love you baby', 'love'))
