import collections
from collections import Counter

#Containers
#list
#set
#dict
#tuple - immutable

#Types
#1 counter 
#2 deque
#3 namedTuple()
#4 orderedDict
#5 defaultdict

c = Counter('gallad')
print(c)
c = Counter(['a','a','b','c','c'])
print(c)
f = Counter ({"a":1,"b":2})
print(c)
d = Counter(cats = 4, dogs = 7)
print(c['pet'])

print(c.most_common(2))

#prints to a list with indices
print(list(c.elements()))

c = Counter(a=4,b=2,c=0,d=-2)
d = Counter(['a','b','b','c'])

#c.subtract(d)
#print(c)
#c.update(d)
#print(c)

print(c+d)
print(c-d)

#intersection
print(c & d)
#union (max elements shown in counters)
print(c|d)