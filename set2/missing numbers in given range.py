def print_missing(arr,low,high):
    hash=set(arr)
    for i in range(low,high+1):
        if i not in hash:
            print(i ,end=" ")

arr=list(map(int,input("enter the elements").strip().split()))
low=int(input("enter the lower range"))
high=int(input("enter the higher range"))
print_missing(arr,low,high)

