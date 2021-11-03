arr=list(map(int,input("enter th earray elements").strip().split()))
odd=0
even=0
n=len(arr)
for i in range(n):
    if arr[i]%2==0:
        even+=1
    else:    
       odd+=1
if odd==n:
    print("The array type is odd") 
elif even==n:
    print("The array type is even")    
else:
    print("Rhe array is mixed tyoe")       
