import time
# 协程一个简单实现
def C():
    while True:
        print("=====C=====")
        yield
        time.sleep(0.5)

def D(c):
    while True:
        print("=====D=====")
        next(c)
        time.sleep(0.5)

if __name__ == "__main__":
    c = C()
    D(c)
