def find_sum(string):
    temp="0"
    sum=0
    for i in string:
        if i.isdigit():
            temp+=i
        else:
            sum+=int(temp)
            temp="0"
    return sum+int(temp)
str1=str(input("enter rhe strin here"))
print(find_sum(str1))                