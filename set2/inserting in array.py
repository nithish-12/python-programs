def insert_(arr,key):
    arr.append(key)
arr=list(map(int,input("enter the elements").strip().split()))
print("The array is",arr)
key=int(input("enter th value to insert"))   
insert_(arr,key)
print("the array after inseertion is : \n",arr)