num1=float(input())
num2=float(input())

num3=float(input())
if num1>num2 and num1>num3:
    greatest=num1
elif num2>num1 and num2>num3:
    greatest=num2
else:
    greatest=num3
print("The greatest number among {} and {} and {} is {}".format(num1,num2,num3,greatest) )         
print(max(num1,num2,num3),"is greatest")