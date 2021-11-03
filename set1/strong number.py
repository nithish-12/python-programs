

num=int(input("enter the number"))
temp=num
sum1=0

while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i+=1
    sum1+=f  
    num//=10
if temp==sum1:
    print("Yes! the number is strong number")
else:
    print("The number is not a strong number")

