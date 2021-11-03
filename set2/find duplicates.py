arr1=list(map(int,input("enter the elements of array").strip().split()))
for i in range(0,len(arr1)):
    for j in range(i+1,len(arr1)):
        if arr1[i]==arr1[j]:
            print(arr1[j],end=" ")