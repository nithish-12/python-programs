n=int(input("enter th enumber"))
l=[]
count=0

for i in range(1,n+1):
    l.append(i)
for i in l:
    if '3' in str(i):
        count+=1
print(count)        


