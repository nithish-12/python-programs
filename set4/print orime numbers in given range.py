lower=int(input("enter the lower range of number"))
higher=int(input("enter the higher range of number"))
for num in range(lower,higher+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,end=" ")



        
