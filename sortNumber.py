import numpy as np
import pandas as pd

randnums= np.random.randint(1,10000,3000)

points = []
num = 1


def findNumber(arr, k):
    arr.sort()
    midpoint = int(len(arr)/2)
    uptimes = 1

    print(arr)
    
    while(1):
        if(arr[midpoint] > k):
            points.append(midpoint)
            
            if(midpoint == 1):
                midpoint -= 1
            else:
                midpoint -= (midpoint/2)

            count = 0
            for point in points:
                if(midpoint == point):
                    count+=1
                if(count > num):
                    return points, "NO"
            
        elif(arr[midpoint] < k):
            uptimes += 1
            points.append(midpoint)
            if((len(arr)/(2**uptimes)) >= 1):
                midpoint += int(len(arr)/(2**uptimes))
            elif midpoint < len(arr)-1:
                if(arr[midpoint] == k):
                    return "YES"
                else:
                    midpoint +=1
            else:
                return "NO"

            count = 0
            for point in points:
                if(midpoint == point):
                    count+=1
                if(count > num):
                    return points,"NO"
            
        else:
            if k == arr[midpoint]:
                return "YES"
            else:
                return points,"NO"

print(findNumber(randnums,9998))