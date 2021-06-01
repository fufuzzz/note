# 进制转换
# 十进制
a = 10
print(a)

# 二进制
b = 0b101
print(b)  # 5

# 八进制

c = 0o27
print(c)

# 十六进制
d = 0x3F
print(d)  # 63

# 对应的函数
print(bin(10))  # 转换成二进制 0b1010
print(oct(10))  # 转换成八进制 0o12
print(hex(1000))  # 转换成十六进制 0x3e8

# 扩展
print(int('101'))  # 101
print(int('101', 2))  # 5, 将101当成二进制数转换成整型
print(int('101', 8))  # 65

# 把八进制27转换成十六进制
b = int('27', 8)
print(b)
c = hex(b)
print(c)

a = [1, 2, 4, 5]
