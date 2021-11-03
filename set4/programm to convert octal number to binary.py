def oct_to_binary(n):
    d=[]
    d.append(int(n,8))
    for i in d:
        print(bin(i).replace('0b',''))
n=str(input("enter the number"))
oct_to_binary(n)      
  