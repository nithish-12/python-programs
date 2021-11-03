num=int(input())
if num<1:
    print("pleasee enter some positive values")
else:
    sum=0
    while(num>0):
     sum+=num
     num-=1
    print(sum)     