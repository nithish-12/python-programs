n=int(input("enter the size of array"))
arr=list(map(int,input("enter the elements").strip().split()))[:n]
print("The max element is ",max(arr),"The min element is ",min(arr))
########################
arr.sort()
print(arr[0],"is minimum")
print(arr[-1],"is maximum")