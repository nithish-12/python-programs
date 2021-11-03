def remove(duplicates):
    final_list=[]
    for i in duplicates:
        if i not in final_list:
            final_list.append(i)
    return final_list
arr_=list(map(int,input("Enter rh elemts").strip().split()))
a=remove(arr_)
print(a)            