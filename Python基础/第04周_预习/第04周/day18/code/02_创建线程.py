# 线程: 主线程, 子线程(分线程)

import _thread
import threading
import time


# 1._thread: 了解
def thread1(*args):
    print('子线程:', threading.current_thread().name)  # 子线程: Dummy -1
    print(args)


def create_thread1():
    print('主线程:', threading.current_thread().name)  # 主线程: MainThread
    # 守护线程: 当主线程退出时子线程会退出
    #       主公 / 忠臣
    _thread.start_new_thread(thread1, ('鲁班', '蔡文姬'))

    time.sleep(0.1)
    print('ok')
    time.sleep(10)
    print('end')


# 2.Thread: 重点掌握
def thread2(*args):  # 子线程
    print('子线程:', threading.current_thread().name)
    print(args)


def create_thread2():
    print('主线程:', threading.current_thread().name)  # 主线程: MainThread
    t = threading.Thread(target=thread2, args=('孙膑', '大乔'), name='王者')
    t.start()

    time.sleep(0.1)
    print('ok')
    time.sleep(1)
    print('end')


import requests


# 3. 自定义线程: 掌握
class MyThread(threading.Thread):
    def __init__(self, name, url):
        super().__init__()
        self.name = name
        self.url = url

    # 需要重写run方法
    def run(self):
        print('子线程:', threading.current_thread().name)

        # 爬取对应rul的内容
        res = requests.get(self.url)
        print(self.name, len(res.text))


def create_thread3():
    MyThread('腾讯', 'https://www.qq.com').start()
    MyThread('百度', 'https://www.baidu.com').start()


if __name__ == '__main__':
    create_thread3()
