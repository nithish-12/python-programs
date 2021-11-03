def capitalize(string):
    result=string=string.title()
    result=" "
    for word in string.split():
        result+=word[:-1]+word[-1].upper()+" "
    return result[:-1]
string=str(input("enter the string"))    
print(capitalize(string))        
