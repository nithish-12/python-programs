def reverse_array(A,start,stop):
    while start< stop:
        A[start],A[stop]=A[stop],A[start]
        start+=1
        stop-=1
A=list(map(int,input("enter rhe ekements").strip().split()))
reverse_array(A,0,len(A)-1)
print(A)
############
def reverse_array(A,start,stop):
    if start>=stop:
        return
    A[start],A[stop]=A[stop],A[start]   
    reverse_array (A,start+1,stop-1)
A=list(map(int,input("enter rhe ekements").strip().split()))
reverse_array(A,0,len(A)-1)
print(A) 
#######################3
def reverse_list(A):
    print(A[::-1])
A=list(map(int,input("enter rhe ekements").strip().split()))
reverse_list(A)




