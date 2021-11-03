num1=int(input("enter the number"))

num2=int(input("enter the number"))
if num1>num2:
    greatest=num1
else:
    greatest=num2
while True:
    if greatest%num1==0 and greatest%num2==0:
        lcm=greatest
        break
    greatest+=1
print(lcm)
########################
num1=int(input("enter the number"))

num2=int(input("enter the number"))  
 
import math
print("The lcm is",math.lcm(num1,num2))


