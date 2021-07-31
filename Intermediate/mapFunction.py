#Map Function
li = {1,2,3,4,5,6,7,8,9,10}

def func(x):
    return x**x

#map function printed 
print(list(map(func,li)))

#list comprehension
print([func(x) for x in li])

#list comprehension for even numbers
print([func(x) for x in li if x%2==0])