
import socket
import threading

# 创建tcp协议的socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('10.36.150.34', 8877))
server.listen(50)

client_list = []

# 每个客户端的子线程: 发送和接收数据
def sock_thread(client, addr):
    while True:
        # 等待接收客户端消息, 会暂停
        data = client.recv(1024)
        print(f'客户端{addr}说: {data.decode()}')

        # 群发
        for c in client_list:
            c.send(f'客户端{addr[0]}说: {data.decode()}'.encode())


# 等待连接
while True:
    print('服务器已启动,等待客户端来连接...')
    client, addr = server.accept()  # 会暂停,会阻塞程序
    print(f"接收到客户端连接: {addr}")

    client_list.append(client)

    # 创建线程: 一个线程对应一个客户端
    t = threading.Thread(target=sock_thread, args=(client, addr))
    t.start()











