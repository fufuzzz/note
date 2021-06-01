import multiprocessing
import os

# 1.使用Process
def fn1(*args):
    print(args)
    print('子进程:', multiprocessing.current_process().name)  # 子进程: Process-1


def create_process1():
    p = multiprocessing.Process(target=fn1, args=('赣深高铁铺轨',))
    p.start()

    print('主进程:', multiprocessing.current_process().name)  # 主进程: MainProcess


# 2.自定义进程
class Myprocess(multiprocessing.Process):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        print('子进程2:', multiprocessing.current_process().name)
        print('子进程pid:', self.pid, os.getpid())
        print('父进程pid:', os.getppid())

def create_process2():
    p = Myprocess('http://www.baidu.com')
    p.start()

    print('p进程的pid:', p.pid)    # 进程id
    print('主进程pid:', multiprocessing.current_process().pid)  # 主进程pid:

    # p.join()  # 等待p进程结束后执行后面的代码
    print(p.is_alive())  # 是否正在进行
    print(multiprocessing.cpu_count())  # 核数


if __name__ == '__main__':
    create_process2()
