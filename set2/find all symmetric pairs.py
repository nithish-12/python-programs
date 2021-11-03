

def find_symmetric(arr1,row):
  hm=dict()
  for i in range(row):
      first=arr1[i][0]
      second=arr1[i][1]
      if second in hm.keys() and hm[second]==first:
          print("(",second,",",first,")")
      else:   
          hm[first]=second
arr1=[[0 for i in range (2)]
         for i in range(5)        
                 ]
arr1[0][0],arr1[0][1]= 11,20
arr1[1][0],arr1[1][1]= 30,40
arr1[2][0],arr1[2][1]= 5,10
arr1[3][0],arr1[3][1]= 40,30
arr1[4][0],arr1[4][1]= 10,5
find_symmetric(arr1,5)

