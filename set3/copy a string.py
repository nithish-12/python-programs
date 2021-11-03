str1=str(input("enter the string"))
str2=str1
str3=str1[:]
str4=" "
str5=" "
for i in str1:
    str4+=i
for i in range(len(str1)):
    str5+=str1[i]
print(str2)
print(str3)
print(str4)
print(str5)        

    
