"""
def show():
print(1)
yield
print(2)
yield
print(3)

s = show()
next(s)
next(s)
next(s)
for i in s:
print(i)
"""

a = (i for i in range(5))
print(type(a))
print(a)