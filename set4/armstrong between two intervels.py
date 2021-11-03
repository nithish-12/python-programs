lower=int(input("enter the lower range of number"))
higher=int(input("enter the higher range of number"))
for num in range(lower,higher+1):
    sum=0
    temp=num
    while(temp>0):
     digit=temp%10
     sum+=digit**3
     temp//=10
    if sum==num:
        print(num,end=" ")