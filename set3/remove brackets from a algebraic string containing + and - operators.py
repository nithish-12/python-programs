def simply(string):
    Len=len(string)
    res=[None]*Len
    i=0
    s=[]
    s.append(0)
    index=0
    while i<Len:
        if string[i]=='+':
            if s[-1]==1:
                res[index]='-'
                index+=1
            else:
                res[index]='+'
                index+=1
        elif string[i]=='-':
            if s[-1]==1:
                res[index]='+'
                index+=1
            else:
                res[index]='-'
                index+=1  
        elif string[i]=="(" and i>0:
            if string[i-1]=="-":
                x=0 if s[-1]==1 else 1
                s.append(x)
            elif string[i-1]=="+":
                s.append(s[-1])
        elif string[i]==")":
            s.pop()
        else:
            res[index]=string[i]
            index+=1
        i+=1
    return res     
s1=str(input("Enter the algebraic expression")) 
r1=simply(s1)
for i in r1:
    if i !=None:
        print(i,end=" ")
    else:
        break          

                


