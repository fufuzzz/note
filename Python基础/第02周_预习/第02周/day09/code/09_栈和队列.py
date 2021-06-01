# 栈: 先进后出,后进先出


# 队列: 先进先出,后进后出
stack = []

# 入栈
stack.append('A')
print(stack)

stack.append('B')
print(stack)

stack.append('C')
print(stack)

stack.append('D')
print(stack)

# 出栈
stack.pop()
print(stack)
print()

# 队列: 先进先出
from collections import deque

# 创建队列
queue = deque()
print(queue)  # deque([])

# 入队列
queue.append('A')
print(queue)

queue.append('B')
print(queue)

queue.append('C')
print(queue)

queue.append('D')
print(queue)


# 出队列
queue.popleft()
print(queue)


queue.popleft()
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)
