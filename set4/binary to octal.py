def bin_to_octal(n):
    d=[]
    d.append(int(n,2))
    for i in d:
        print(oct(i).replace('0o',''))
n=str(input("enter rhe number"))
bin_to_octal(n)        