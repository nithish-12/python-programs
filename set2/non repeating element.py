
def non_repeating_elements(arr,n):
    d=[]
    mp={}
    for i in range(n):
        if arr[i] not in mp:
            mp[arr[i]]=0
        mp[arr[i]]+=1
    for x in mp:
        if mp[x] ==1:
            print(x, end=" ")  
arr=list(map(int,input("enter rhe array ").strip().split()))
n=len(arr)
non_repeating_elements(arr,n)

                 