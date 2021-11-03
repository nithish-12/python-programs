def max_sub_array(arr):
    max_so_far=0
    max_ending_here=1
    min_ending_here=1
    flag=0
    n=len(arr)
    for i in range(n):
        if arr[i]>0:
            max_ending_here=max_ending_here*arr[i]
            min_ending_here=min(min_ending_here*arr[i],1)
            flag=1
        elif arr[i]==0 :
                max_ending_here=1
                min_ending_here=1
        else:
            temp=max_ending_here
            max_ending_here=max(min_ending_here*arr[i],1)
            min_ending_here=temp*arr[i]
        if max_so_far<max_ending_here:
            max_so_far=max_ending_here
    if flag==0 and max_ending_here==0:
        return 0
    return max_so_far
arr=list(map(int,input("enter the elements").strip().split()))
print(max_sub_array(arr))       


