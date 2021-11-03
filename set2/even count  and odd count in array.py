def count_even_or_odd(arr,n):
    even_=0
    odd_=0
    for i in range(n):
        if arr[i]&1==1:
            odd_+=1
        else:
            even_+=1
    print("the odd eleemts count is",odd_)
    print("the veen elements count is",even_)        
arr_=list(map(int,input("enter th elements in array").strip().split()))
n=len(arr_) 
count_even_or_odd(arr_,n)
               