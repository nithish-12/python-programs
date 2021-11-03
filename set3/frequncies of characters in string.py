string=str(input("enter th etsring"))
c={}
for i in string:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print("per char frequencies in {} is {}".format(string,str(c))) 
############


import collections
string=str(input("enter th etsring"))
freq=collections.Counter(string)
print("per char frequencies in {} is {}".format(string,str(freq))) 
