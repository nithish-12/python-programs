num=int(input("enter"))
temp=num
rev=0
while(num):
    digit=num%10
    rev=rev*10+digit
    num//=10
print("The reversed number is %d"%rev)    