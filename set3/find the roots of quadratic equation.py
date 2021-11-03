import math
def findroots(a,b,c):
    dis=b*b-4*a*c
    sqrt_val=math.sqrt(abs(dis))
    if dis>0:
        print("Real and distinct roots")
        print((-b-sqrt_val)/(2*a))
        print((-b+sqrt_val)/(2*a))
    elif dis==0:
        print("The roots are REal") 
        print(-b/(2*a))
    else:
        print("The roots are complex") 
        print(-b/(2*a),"-i",sqrt_val) 
        print(-b/(2*a),"+i",sqrt_val) 
a=int(input("enter rthe number"))  
b=int(input("enter rthe number"))  
c=int(input("enter rthe number")) 
if a==0:
    print("Input cannot be a quadratic function")
else:
    findroots(a,b,c)   
##########################3
import cmath
a=int(input("enter rthe number"))  
b=int(input("enter rthe number"))  
c=int(input("enter rthe number"))     
d=b*b-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print("The solution are {0} and {1}".format(sol1,sol2))





