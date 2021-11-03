def remove_vowels(string):     
     lst=['a','e','i','o','u']
     for x in string.lower():
         if x in lst:
             string=string.replace(x,"")
     print(string)        
string=str(input("entre the string"))
remove_vowels(string)
#############3

import re
def remove_vowels(string):
    return re.sub("[aeiouAEIOU]","",string)
string=str(input("entre the string"))
print(remove_vowels(string))   

             