num=int(input("enter the number here"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("The number is not prime")
            print(i,"times",num//i,"is",num)
            break
        else:
            print("yes!it is prime number") 
            break
else:
    print("No! it is not prime")               