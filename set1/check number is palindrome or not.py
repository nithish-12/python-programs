n=int(input("Enter rhe number here"))
temp=n
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n//=10
if temp==rev:
    print("Yes! it is palindrome")
else:
    print("No!it is not palindrome")        