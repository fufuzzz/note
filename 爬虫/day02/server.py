# 1,导入socket包
import socket
import re
# 2,创建tcp的socket套接字
s = socket.socket()

# 3,绑定ip和端口
s.bind(('127.0.0.1', 8000))

# 4.允许有多少个客户端连接服务器
s.listen(5)

# 5,监听有没有客户端连接服务器
# 它是一个阻塞的,如果没有客户端连接,一直等待客户端的连接
# 如果游客户端连接,那么返回值有两个,
# 第一个值就是 以后和客户端收发数据的对象
# 第二个值就是 连接的客户端的ip地址
while True:  # 服务器不关闭,允许多个客户端连接
    sock, address = s.accept()

    # 6,接收客户端传递的数据
    # recv方法也是阻塞的,如果客户端没有发数据,一直等待
    # 接收的数据默认是byte类型
    # 可以转成字符串
    recv_data = sock.recv(1024).decode()
    print(recv_data)

    # 通过正则获取请求方式和请求路径
    res = re.match(r'(.+?)/(.+?)HTTP', recv_data)
    method = res.group(1).strip()
    path = '/'+res.group(2).strip()
    print('-*------------*--')
    print(res.group(1).strip())
    print(res.group(2).strip())
    print(path)
    print('-*------------*--')


    # 7,根据接收到的数据,处理请求逻辑
    # 模拟服务器根据接收的数据,处理请求
    # 1,响应行
    part1 = 'HTTP/1.1 200 o\r\n'
    # 2,响应头
    part2 = 'content-type:text/html;charset="utf-8"\r\n'
    # 3,空行
    part3 = '\r\n'

    if path == '/':
    # 4,响应体
        part4 = '''
        <form method='get' action='http://127.0.0.1:8000/data'>
        用户名: <input  type='text' name='username'> <br>
        密码: <input type='password' name='pwd'> <br>
        <input type='submit' value='提交'>
        <form/>
        '''
    elif path.startswith('/data'):
        # 获取用户名和密码
        ret = re.search(r"username=(.+?)&pwd=(.+)HTTP/1.1", recv_data)
        username = ret.group(1).strip()
        pwd = ret.group(2).strip()
        print('-*------------*--')
        print(username)
        print(pwd)
        print('-*------------*--')
        # 判断用户名和密码对不对
        # 如果用户名是root and 密码是 123456,那么返回登录成功的文本
        if username == 'root' and pwd =='123456':
            part4 = '登录成功'
        # 如果不匹配,返回登录失败
        else:
            part4 = '登录失败'


    send_data = part1 + part2 + part3 + part4

    # send_data = 'hello' + recv_data

    # 8, 把数据返回给客户端
    # 传输的数据一定是byte类型
    sock.send(send_data.encode())

    # 9,传输完数据后,可以关闭通信通道 sock 和服务器s
    sock.close()
    # s.close()
