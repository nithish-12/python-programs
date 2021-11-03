def count_distinct(arr,n):
    hashset=set()
    res=0
    for i in range(n):
        if arr[i] not in hashset:
            hashset.add(arr[i])
            res+=1
    return res
arr=list(map(int,input("enter the lelements").strip().split()))
n=len(arr) 
print(count_distinct(arr,n))           