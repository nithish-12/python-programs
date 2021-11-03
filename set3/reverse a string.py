def reverse(string):
    string=string[::-1]
    #string="".join(reversed(string))
    return string
string=str(input("enter"))
a=reverse(string) 
print(a)  
#############
def createstack():
    stack=[]
    return stack
def size(stack):
    return len(stack)
def is_empty(stack):
    if size(stack)==0:
        return True
    else:
        return False
def push(stack,item):
    stack.append(item)
def pop(stack):
    if is_empty(stack):
        print("underflow!")
    return stack.pop()
def reverse(string):
    n=len(string)
    s=createstack()
    for i in range(0,n):
        push(s,string[i])
    string1=" "
    for i in range(n):
        string1+=pop(s)
    return string1 
string=str(input("enter the string here"))
print(reverse(string))                  