#Lambda Tutorial
def func(x):
    func2 = lambda x: x+5
    return func2(x)+85

func3 = lambda x,y=4: x+y

print(func(2))
print(func3(4,5))


#lambda with map and filter
a = [1,2,3,4,5,6,7,8,9,10]

newList = list(map(lambda x:x+5,a))
print(newList)

newList2 = list(filter(lambda x:x%2==0,a))
print(newList2)