num=int(input("Enter rhe number"))
temp=num
sum=0
ord=len(str(num))
while(num>0):
    digit=num%10
    sum+=digit**ord
    num//=10
if sum==temp:
    print("Yes! it is armstrong")  
else:
    print("Not armstrong")      