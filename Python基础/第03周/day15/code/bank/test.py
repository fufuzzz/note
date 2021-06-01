import pickle
fp2 = open('2.txt', 'rb')
p2 = pickle.load(fp2)
print(p2, type(p2))  # {'name': '刘德华', 'age': 62}
fp2.close()
# print(p2['888866662144'].card.money)
# print(p2['888866664242'].card.money)

a = 100

b = False

print(a * b > -1)


num1 = 1 and 2

num2 = True or False

result = num1*num2 + 3
print(result)
print(("1" + "1"))

