from multiprocessing import Process,Manager

# lis = []
# dic = []

def run1(lis, dic):
    lis.append('run1')
    dic['a'] = 'a'


def run2(lis, dic):
    lis.append('run2')
    dic['b'] = 'b'


if __name__ == '__main__':

    with Manager() as manager:

        # 创建manger对象的共享内存
        # 共享内存有两种方式,一种是列表,一种是字典共享
        lis = manager.list()
        dic = manager.dict()

        # 创建进程
        p1 = Process(target=run1, args=(lis, dic))
        p2 = Process(target=run2, args=[lis, dic])

        # 执行进程
        p1.start()
        p2.start()

        # 阻塞,必须等待在这两个进程执行完之后, 再打印lis
        p1.join()
        p2.join()

        print(lis)
        print(dic)
        print(type(lis))