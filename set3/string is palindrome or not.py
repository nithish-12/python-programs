def is_palindrome(s):
    return s==s[::-1]
string=str(input("enter the string"))
ans=is_palindrome(string)
if ans:
    print("yes") 
else:
    print("No")
###############
def is_palindrome(s):
    rev="".join(reversed(s))
    if s==rev:
        return True
    return False

string=str(input("enter the string"))
ans=is_palindrome(string)
if ans:
    print("yes") 
else:
    print("No")     
