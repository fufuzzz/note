# + :可以用来拼接,用于 字符串,元组,列表

print('hello' + 'world')
print(('good', 'yes') + ('hi', 'ok'))
print([1, 2, 3] + [4, 5, 6])

# -:只能用户集合,求差集
print({1, 2, 3} - {3})

# *:可以用于字符串元组列表,表示重复多次.不能用于字典和集合
print('zhangsan' in {'name': 'zhangsan', 'age': 18, 'height': '180cm'})
print('name' in {'name': 'zhangsan', 'age': 18, 'height': '180cm'})
print(3 in {3, 4, 5})

# nums = [19, 82, 39, 12, 34, 58]
# nums = (19, 82, 39, 12, 34, 58)
nums = {19, 82, 39, 12, 34, 58}
# 带下标的遍历
en = enumerate(nums)
for i, e in en:
    print('第%d个数据是%d' % (i, e))

person = {'name': 'zhangsan', 'age': 18, 'height': '180cm'}
for i, x in enumerate(person):
    print(i, x)

