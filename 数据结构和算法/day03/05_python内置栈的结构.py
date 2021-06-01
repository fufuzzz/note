import queue

q = queue.LifoQueue()

q.put(10)
q.put(20)
q.put(30)
q.put(40)

print(q.get())
print(q.qsize()) # 长度