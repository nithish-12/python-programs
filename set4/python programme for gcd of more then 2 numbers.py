def fin_gcd(x,y):
    while y:
        x,y=y,x%y
    return x
l=list(map(int,input("enter rhe numbers in list").strip().split()))
num1=l[0]
num2=l[1]
gcd=fin_gcd(num1,num2)
for i in range(2,len(l)):
    gcd=fin_gcd(gcd,l[i])
print(gcd)    
