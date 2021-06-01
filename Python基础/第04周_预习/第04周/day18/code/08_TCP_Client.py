
import socket
import threading

# 创建tcp协议的socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.36.150.34', 8877))

# 发送数据
def send_thread():
    while True:
        # 发送消息给服务器
        data = input('客户端说:')
        client.send(data.encode())


# 接收数据
def recv_thread():
    while True:
        # 接收服务端数据
        data2 = client.recv(1024)
        print(data2.decode())


threading.Thread(target=send_thread).start()
threading.Thread(target=recv_thread).start()

