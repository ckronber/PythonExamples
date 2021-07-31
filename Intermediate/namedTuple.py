import collections
from collections import namedtuple

Point = namedtuple('Point', 'x y z h')
Point2 = namedtuple('Point2', ['x','y','l'])
newP = Point(3,4,5,8)
newP2 = Point2(3,4,5)
print(newP2)

Point3 = namedtuple('Point3', {'x':0,'y':0,'z':0})
newP3 = Point3(3,4,5)
print(newP3)
print(newP3._asdict())
print(newP3._fields)

print(newP3._replace(x=6))

p2 = Point.make(['a','b','c'])
print(p2)