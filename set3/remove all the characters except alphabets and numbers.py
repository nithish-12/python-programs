string=str(input("enter the string"))
s=""
for i in string:
    if i.isalnum():
        s+=i
print(s) 
##############################3    

get_list=list([val for val in string if val.isalpha() or val.isnumeric()])
result="".join(get_list)
print(result)
