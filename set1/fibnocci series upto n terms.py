
a=0
b=1
sum=0
count=1
n=int(input("enter rhe number"))


while(count<=n):
    print(sum)
    count+=1
    a=b
    b=sum
    sum=a+b
