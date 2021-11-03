n=int(input("Enter rhhe sixe of array"))
arr1=list(map(int,input("Enter the elements").strip().split()))[:n]
arr2=list(map(int,input("Enter the elements").strip().split()))[:n]
sum=0
  
arr1.sort(reverse=True)
arr2.sort(reverse=True)
for i in range(0,n):
    sum=sum+(arr1[i]*arr2[i])
print("MAXimum scalar product",sum)    
