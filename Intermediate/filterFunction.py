#Filter Function

def add7(x):
    return x+7

def isOdd(x):
    return x%2 == 1

a = [1,2,3,4,5,6,7,8,9,10]

#filter takes a function and an iterable item
b = list(filter(isOdd,a))

c = list(map(add7,b))
print(c)