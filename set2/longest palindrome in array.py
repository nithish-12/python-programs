def is_palindrome(n):
    divisor=1
    while(n/divisor>=10):
        divisor=divisor*10
    while(n!=0):
        leading=n//divisor
        trailing=n%10
        if leading!=trailing:
            return False
        n=(n%divisor)//10
        divisor//=100
    return True
def longest_palindrome(arr,n):
    arr.sort()
    for i in range(n-1,-1,-1):
        if is_palindrome(arr[i]) :
            return arr[i]
    return -1
arr=list(map(int,input("enter the elements in array").strip().split()))  
n=len(arr)
print(longest_palindrome(arr,n))                     


















