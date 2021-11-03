def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
r=int(input("enter rhe number of ceats avialable"))
n=int(input("enter the no of people"))
if n<r:
    temp=n
    n=r
    r=temp
num=fact(n)
den=fact(n-r)
p=int(num/den) 
print("The number of ways ",p)           