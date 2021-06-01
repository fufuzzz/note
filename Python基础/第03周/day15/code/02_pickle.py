
# pickle模块
#   作用: 直接将列表/字典存入文件中
# 持久化: 永久存储
import pickle


# 存入
p = {'name': '刘德华', 'age': 62}
fp = open('person.txt', 'ab')
pickle.dump(p, fp)
fp.close()


# 读取
fp2 = open('person.txt', 'rb')
p2 = pickle.load(fp2)
print(p2, type(p2))  # {'name': '刘德华', 'age': 62}
fp2.close()
