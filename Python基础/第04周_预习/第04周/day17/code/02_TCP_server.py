

import socket

# 1.创建tcp协议的socket对象
# server = socket.socket()
# 参数:
# socket.AF_INET: IPV4
# socket.SOCK_STREAM: TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.绑定ip和port
server.bind(('10.36.150.34', 8888))

# 3.设置监听数量,连接数量
server.listen(5)

# 4.等待连接
print('服务器已启动,等待客户端来连接...')
client, addr = server.accept()  # 会暂停,会阻塞程序
print(f'接收到客户端连接: {addr}')

# 5.发送和接收消息
while True:
    # 等待接收客户端消息,会暂停
    data = client.recv(1024)
    print(f'客户端{addr}说: {data.decode()}')

    # 发送消息给客户端
    client.send("收到".encode())
