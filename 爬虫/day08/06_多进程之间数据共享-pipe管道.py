from multiprocessing import Process,Manager,Queue,Pipe

# lis = []
# dic = []

def run1(obj1):
    # send() 发数据
    obj1.send('run1')


def run2(obj2):
    # recv()收数据
    print(obj2.recv())



if __name__ == '__main__':

    obj1, obj2 = Pipe()

    # 创建进程
    p1 = Process(target=run1, args=(obj1, ))
    p2 = Process(target=run2, args=(obj2, ))

    # 执行进程
    p1.start()
    p2.start()

    # 阻塞,必须等待在这两个进程执行完之后, 再打印lis
    p1.join()
    p2.join()


