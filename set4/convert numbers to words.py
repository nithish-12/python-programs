def covert_number_to_words(num):
    l=len(num)
    if l==0:
        print("empty")
        return
    if l>4:
        print('it should not be greate then four digitd') 
        return
    single_digits=['zero','one','two','three','four','five','six','seven','eight','nine']
    two_digits=[' ','ten','eleven','tweleve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen']
    tens_multiples=['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninghty']
    tens_power=['hundred','tousand']
    if l==1:
        print(single_digits[ord(num[0])-48])
        return
    x=0
    while(x<len(num)):
        if l>=3:
            if ord(num[x])-48!=0:
                print(single_digits[ord(num[x])-48],end=" ")
                print(tens_power[l-3],end=" ")
            l-=1        
        else:
            if ord(num[x])-48==1:
                sum=ord(num[x])-48 + ord(num[x+1])-48
                print(two_digits[sum])
                return
            elif ord(num[x])-48==2 and ord(num[x+1])-48==0:
                print("Twenty")
                return
            else:
               i=ord(num[x])-48
               if i>0:
                  print(tens_multiples[i],end=" ")
               else:
                   print(" ",end=" ")
               x+=1
               if(ord(num[x])-48!=0):
                   print(single_digits[ord(num[x])-48])
        x+=1
num=str(input("Enter the number"))
covert_number_to_words(num)                       







