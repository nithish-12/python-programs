def palndrome(rows):
    for i in range(0,rows+1):
        for j in range(i,rows+1):
            print(" ",end=" ")
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(i-1,0,-1):
            print(j,end=" ")
        print()
n=int(input("Enter the number"))
palndrome(n)        
