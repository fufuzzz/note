import queue

q = queue.Queue()

q.put(10)
q.put(20)
q.put(30)
q.put(40)

print(q.get())
print(q.qsize()) # 长度

# 优先级队列
q = queue.PriorityQueue()
q.put((1, 'a'))
q.put((10, 'b'))
q.put((5, 'c'))

print(q.get())
print(q.get())
print(q.get())