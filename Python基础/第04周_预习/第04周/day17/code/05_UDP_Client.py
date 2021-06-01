import socket

# 1.创建基于UDP协议的socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2.发送和接收消息
while True:
    # 发送消息
    data = input('客户端说:')
    client.sendto(data.encode(), ('10.36.150.34', 8877))

    # 接收服务端发过来的数据
    data, server_addr = client.recvfrom(1024)
    print(f'->服务端({server_addr}): {data.decode()}')

