arr_=list(map(int,input("enter the elements in original arrar").strip().split()))

for i in range(0,len(arr_)):
    for j in range(i+1,len(arr_)):
        temp=arr_[i]
        arr_[i]=arr_[j]
        arr_[j]=temp
for i in range(0,len(arr_)):
    print(arr_[i],end=" ")
##############3
arr_.sort()
print(arr_)   
