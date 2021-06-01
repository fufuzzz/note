
import socket

feiqiu = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送飞秋信息
# 1: 飞秋版本
# 2: 包名
# 赵本山: 用户名
# ZBS: 主机名
# 32: 表示发送消息
# 我的二人转怎么样: 发送内容
data = '1:2:赵本山:ZBS:32:我的二人转怎么样'
for i in range(3):
    feiqiu.sendto(data.encode('GBK'), ('10.36.150.52', 2425))
