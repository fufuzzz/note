# 1, 导入socket包
import socket

# 2,创建socket套接字
c = socket.socket()

# 3,连接服务器
c.connect(('127.0.0.1', 8000))

# 4,发送数据
con = input(">>")
c.send(con.encode())

# 5,收数据
recv_data = c.recv(1024)

# 6,打印数据
print(recv_data.decode())

# 7.关闭连接
c.close()