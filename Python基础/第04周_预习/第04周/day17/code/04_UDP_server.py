
import socket

# 1.创建基于UDP协议的socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2.绑定ip和port
server.bind(('10.36.150.34', 8877))

# 3. 接收和发送消息
while True:
    # 接收消息,会暂停
    data, client_addr = server.recvfrom(1024)
    print(f'->客户端({client_addr}): {data.decode()}')

    # 发送消息给客户端
    server.sendto('收到'.encode(), client_addr)