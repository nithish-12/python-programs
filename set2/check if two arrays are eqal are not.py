def are_arrau_equal(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    if n!=m:
        
        print("the two array sare not equal")
    
    arr1.sort()
    arr2.sort()
    for i in range(0,n-1):
        if arr1[i]!=arr2[i]:
            return False
    return True
arr1=list(map(int,input("enter the input of the array for first array").strip().split()))
arr2=list(map(int,input("enter the input of the array for second array").strip().split()))
print(are_arrau_equal(arr1,arr2))