def find_sum(arr,n,sum):
    for i in range(n-1):
        s=dict()
        for j in range(i+1,n):
            x=sum-(arr[i]+arr[j])
            if x in s.keys():
                print(x,arr[i],arr[j])
            else:
                s[arr[j]]=1
arr=list(map(int,input("enter th elements").strip().split())) 
sum=int(input("enter the elemet"))
n=len(arr)
find_sum(arr,n,sum)                   
