arr=list(map(int,input("enter the lements of array").strip().split()))

key=int(input("enter the elemnt"))
if key in arr:
    print(arr.index(key))
else:
    print("eleemnt not found")    

##########
def searh_index(arr,key,n):
    for i in range(n):
        if arr[i] ==key:
            return i
    return -1
arr=list(map(int,input("enter the lements of array").strip().split()))
n=len(arr)
key=int(input("enter the elemnt"))
index=searh_index(arr,key,n) 
if index!=-1: 
    print("the element is at",(index+1))
else:
    print("element not found") 
