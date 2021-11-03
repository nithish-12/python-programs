def is_subset(arr1,m,arr2,n):
    hashset=set()
    for i in range(m):
        hashset.add(arr1[i])
    for i in range(n):
        if arr2[i]in hashset:
            continue
        else:
            return False
    return True
arr1=list(map(int,input("Enter the elememts").strip().split()))
m=len(arr1)
arr2=list(map(int,input("Enter the elememts").strip().split()))
n=len(arr2)
if(is_subset(arr1,m,arr2,n)):
    print("yes arr2 is subset")
else:
    print("Not a subset")    

