def firstnonrepeating(string):
    d=[]
    c={}
    for i in string:
        if i in c:
          c[i]+=1
        else:
            c[i] =1
            d.append(i)
    for i in d:
        if c[i]==1:
            return i
    return None
string=str(input("Enter the string here"))
a=firstnonrepeating(string) 
print(a)                   
