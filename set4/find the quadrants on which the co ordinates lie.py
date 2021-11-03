def quadrant(x,y):
    if x>0 and y>0:
        print("first quadrant")
    elif x<0 and y>0:
        print("second quadrat")  
    elif x<0 and y<0:
        print("third quadrant")
    elif x>0 and y<0:
        print("fourth quadrat")
    elif x==0 and y>0:
        print("positive y axis")
    elif x>0 and y==0:
        print("positive x axis") 
    elif x==0 and y<0:
        print("nehative y axis")
    elif x<0 and y==0:
        print("negative x axis")  
    else:
        print("origin")
x=int(input()) 
y=int(input()) 
quadrant(x,y)


