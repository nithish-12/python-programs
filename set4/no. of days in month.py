class solution(object):
    def number_of_days(self,y,m):
        leap=0
        if y%4==0:
            leap=1
        elif y%100==0:
            leap=0
        elif y%400:
            leap=1
        if m==2:
            return 28+leap  
        lst=[1,3,5,7,8,10,12]
        if m in lst:
            return 31
        else:
            return 30
s=solution()
y=int(input("Enter the year"))
m=int(input("enter rhe month"))
print(s.number_of_days(y,m))                              