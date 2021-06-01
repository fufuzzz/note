# 偏函数: 了解

print(int('1010'))  # 1010
print(int('1010', base=2))  # 10
print(int('1010', base=8))  # 520

import functools
# 偏函数: 将参数默认值修改
int2 = functools.partial(int, base=2)

print(int2('1010'))  # 10

