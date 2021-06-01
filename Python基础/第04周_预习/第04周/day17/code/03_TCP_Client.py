
import socket

# 1.创建tcp协议的socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.主动连接服务器端
client.connect(('10.36.150.34', 8888))

# 3.发送和接收消息
while True:
    # 发送消息给服务器
    data = input('客户端说:')
    client.send(data.encode())

    # 接收服务器数据
    data2 = client.recv(1024)
    print(f"-->服务器说:{data2.decode()}")