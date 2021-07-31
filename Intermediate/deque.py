import collections
from collections import deque

#deque is faster than a list to add elements to the end and beginning
d = deque("hello")
print(d)

d.append('4')
d.append('5')
d.appendleft('5')

d.pop()
d.popleft()
print(d)

d.clear()
print(d)

#add multiple things into a deque
d.extend('456')
d.extend(['1','2','3'])
d.extendleft('hey')
print(d)

#positive rotates to the right negative rotates to the left
d.rotate(-2)
print(d)

# can set the max length of the deque
e = deque('hello', maxlen=5)
print(e)
e.extend([1,2,3])
print(e)
