import numpy as np
from pandas import Series

list = [1, 2, 3, 4]
n = np.array(list)
s = Series(data=n)
# print(s)
# print({n: list.index(n) for n in list})
# print({n: list.index(n) for n in n})
# print({n: s[s.values==n].index[0] for n in s})
# print(s.index)
# print(s[s.values==3].index[0])
#
#
# print(s.index[s.values==3][0])
# print(s.values==3)
# print(np.where(n==2)[0][0])