import math
def get_sum(arr):
    n=len(arr)
    hashset=set()
    sum=0
    for i in range(n):
        hashset.add(arr[i])


    for i in range(n):
       sqr_current=math.sqrt(arr[i])
       if math.floor(sqr_current)!=math.ceil(sqr_current):
        continue
       if sqr_current in hashset:
         sum+=int(sqr_current*sqr_current)
    return sum
arr_=list(map(int,input("Eter the elemnts in array").strip().split()))
print(get_sum(arr_))  
