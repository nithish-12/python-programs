f1_num=int(input("enter rthe number"))  
f1_den=int(input("enter rthe number"))  
f2_num=int(input("enter rthe number"))
f2_den=int(input("enter rthe number"))  
if f1_den==f2_den:
    fraction=f1_num+f2_num
    print("The addtion of two fraction is",fraction,'/',f2_den)
else:
    fraction=(f1_num*f2_den)+(f2_num*f1_den)
    print("The addition of two fractions is",fraction,'/',f1_den*f2_den)


