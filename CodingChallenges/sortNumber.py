import numpy as np
import pandas as pd

randnums= np.random.randint(1,10000,3000)

points = []
num = 1

def findNumber(arr, k):
    arr.sort()
    midpoint = int(len(arr)/2)
    TotalVal = int(midpoint)

    print(arr)
    
    while(TotalVal < (len(arr)-1) and (TotalVal > 0)):
        if(arr[TotalVal] > k):
            points.append(TotalVal)
            if(midpoint >= 1):
                midpoint = int(midpoint/2)
                TotalVal -= midpoint
            else:
                TotalVal -= 1
            
            if(arr[TotalVal] == k):
                return "YES"

            count = 0
            for point in points:
                if(TotalVal == point):
                    count+=1
                if(count > num):
                    return "NO"

        elif(arr[TotalVal] < k):
            points.append(TotalVal)
            if(midpoint >= 1):
                midpoint = int(midpoint/2)
                TotalVal += midpoint
            else:
                TotalVal += 1

            if(arr[int(TotalVal)] == k):
                return "YES"

            count = 0
            for point in points:
                if(TotalVal == point):
                    count+=1
                if(count > num):
                    return "NO"
    return "NO"

print(findNumber(randnums,5554))