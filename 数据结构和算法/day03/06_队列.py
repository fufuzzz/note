class Queue():

    # 创建一个空的队列
    def __init__(self):
        self.item = []

    # 往队列中添加一个item元素
    def enqueue(self, item):
        self.item.append(item)

    # 从对列头部删除一个元素
    def dequeue(self):
        return self.item.pop(0)

    # 判断一个队列是否为空
    def is_empty(self):
        return self.item == []

    # 返回队列的大小
    def size(self):
        return len(self.item)
