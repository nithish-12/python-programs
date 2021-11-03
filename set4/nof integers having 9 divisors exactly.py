def number_of_fact(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count
def countNumbers(n):
    count=0 
    for i in range(1,n+1):
        if number_of_fact(i)==9:
            count+=1
    return count
n=int(input("enter rhe number")) 
print(countNumbers(n))                     