
mystring = "supercalofragilisticexpialodocious"
i = 0

for s in mystring:
    if(s == "i"):
        i+=1

print("There are: " + str(i) +" i's in the word")

#Fibonacci series:
print("Fibbonaci Series less than 10:\n")
a,b = 0,1
while a < 10:
    print (a)
    a,b = b, a+b