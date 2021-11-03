from math import gcd as __gcd
def is_divisible(num,x,y):
    while(num%x)==0 or (num%y)==0:
        if num%x==0:
            num//=x
        if num%y==0:
            num//=y
    if num>1:
        return False
    return True

def is_possible(arr,x,y,n):
    gcd=arr[0]
    for i in range(1,n):
        gcd=__gcd(gcd,arr[i])
    for i in range(n):
        if(is_divisible(arr[i]//gcd,x,y))==False:
            return False
    return True
arr=list(map(int,input("Enter rhe lements in the array").strip().split()))
n=len(arr)
x=int(input("Enter the value of x"))
y=int(input("Enter the value of y")) 
if is_possible(arr,x,y,n):
    print("yes")
else:
    print("NO")      

