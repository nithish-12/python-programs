import math
def isptime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False  
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True 
def is_possible(n):
    if isptime(n) and isptime(n-2):
        return True
    else:
        return False
n=int(input("enter the number here"))
if is_possible(n)==True:
    print("yes")
else:
    print("No")            
