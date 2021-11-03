arr_=list(map(int,input("enter the elements of array").strip().split()))
element_counts={}
for i in arr_:
    if i in element_counts:
        element_counts[i]+=1
    else:
        element_counts[i]=1
for key,value in element_counts.items():
    print(f"{key}:{value}") 
    ###########
import collections
arr_=list(map(int,input("enter the elements of array").strip().split()))
element_count=collections.Counter(arr_)
for key,value in element_count.items():
    print(f"{key}:{value}")
