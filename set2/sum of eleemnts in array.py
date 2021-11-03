def _sum(arr):
    sum=0
    for i in arr:
        sum+=i
    print("The sum of all eleemnts in array  is",sum)
arr=list(map(int,input("enter the elements").strip().split()))
_sum(arr)      

######
arr=list(map(int,input("enter the elements").strip().split()))
print("the sum of all elements in your array is ",sum(arr))







