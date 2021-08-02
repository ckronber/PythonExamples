import datetime
import sys
import math
import time
import re

l = 1
h = 10
i = 0
luckyNumbers = 0

startTime = datetime.datetime.now()

for i in range(l,h+1):
    number = int(math.log10(h))+1
    print(int((168%100)/10))
    for j in range(number):
        if(math.pow(10,j) == 6):
           luckyNumbers += 1
        if(math.pow(10,j) == 8):
            if(luckyNumbers == 0):
                luckyNumbers+=1
            else:
                luckyNumbers-=1

    #if("6" in str(i) and "8" in str(i)):
    #    continue
    #elif("6" in str(i)):
    #    luckyNumbers+=str(i)):
    #    luckyNumbers+=1
    #elif("8" in str(i)):
    #    luckyNumbers+=str(i)):
    #    luckyNumbers+=1

print(luckyNumbers)

finishTime = datetime.datetime.now()
elapsedTime = (finishTime-startTime)
totalMicroseconds = elapsedTime.microseconds

print("\n" + str(totalMicroseconds) + " Microseconds to complete \n")