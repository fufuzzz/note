
# Python函数:
#   内置函数/标准函数/: print(), len()
#   自定义函数: 自己写的函数

# 列表的增删改查
#   增: append, insert, extend
#   删除: pop, remove, clear, del
#   改: ages[0] = 11
#   查: ages[0], ages[:], 遍历

# 增:给列表增加元素
# append(n): 在列表的末尾添加元素

nums = [3, 4, 5]
nums.append(6)
print(nums)

# insert(i, n): 在列表的下标为i的位置插入一个元素n
nums.insert(1, 2)
print(nums)

# extend(): 将另一个序列中的所有元素添加到列表中
nums.extend([7, 8, 9])
# nums.append([7, 8, 9])  # [3, 2, 4, 5, 6, [7, 8, 9]]
print(nums)


# 删
stars = ['贾乃亮', '鹿晗', '鹿晗', 'PGOne', '李小璐', '李晨', '范冰冰']

# pop(i): 弹出下标为i的元素
n = stars.pop()  # 默认弹出最后一个
# n = stars.pop(1)
# print(stars)
# print(n)

# remove(n): 删除指定的第一个元素

# count(n): 统计n在列表中出现的次数
for i in range(stars.count('鹿晗')):
    stars.remove('鹿晗')
print(stars)

# clear(): 清空列表
ages = [1, 2, 3, 4]
ages.clear()
print(ages)  # []

# 改
ages = [1, 2, 3, 4]
ages[0] = 99
print(ages)

# 查
print(ages[0])
# 使用循环
