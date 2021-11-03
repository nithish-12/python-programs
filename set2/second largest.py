def find_len(list1):
    length=len(list1)
    list1.sort()
    print("he second largest is",list1[-2])
list1=list(map(int,input("enter the elelemts in array").strip().split()))
find_len(list1)    