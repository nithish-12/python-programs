def toggleCharacters(string):
    for i in range(len(string)):
        if string[i]>='A' and string[i]<='Z':
            string=string[:i]+chr(ord(string[i])+ord('a')-ord('A'))+string[i+1:]
        elif string[i]>='a' and string[i]<='z':
            string=string[:i]+chr(ord(string[i])+ord('A')-ord('a'))+string[i+1:]
    return string
string=str(input("enter rhes tring"))
a=toggleCharacters(string)
print(a)               
