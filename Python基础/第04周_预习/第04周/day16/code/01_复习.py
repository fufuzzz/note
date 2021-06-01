
# pickle模块

import pickle

# 存
d = {'name': '张三', 'age': 33}
fp = open('pickle.txt', 'wb')
pickle.dump(d, fp)
fp.close()

# 取
fp = open('pickle.txt', 'rb')
d2 = pickle.load(fp)
print(d2)  # {'name': '张三', 'age': 33}
fp.close()

#