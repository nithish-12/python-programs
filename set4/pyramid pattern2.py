def print_triangle(n):
    k=n-1
    for i in range(n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
           print("*",end=" ")
        print(" ")
n=int(input("Enter the number"))
print_triangle(n)    
#o/p
#    *  
#   * *
#  * * *
# * * * *
#* * * * *

