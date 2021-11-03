num=int(input("enter the number"))
exponent=int(input("enter the exponent"))
power=1
for i in range(1,exponent+1):
    power=power*num
print(power) 

###
num=int(input("enter the number"))
exponent=int(input("enter the exponent"))
power=1
i=1
while(i<=exponent):
    power=power*num
    i+=1
print(power)  
##

import math
num=int(input("enter the number"))
exponent=int(input("enter the exponent"))
print(int(math.pow(num,exponent)))

