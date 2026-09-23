N=int(input("Enter range from 1"))
for i in range(1,N+1):
    list1=[]
    for j in range(1,i+1):
        if i%j==0:
            list1.append(j)
    if len(list1)==2:
        print(i)  
          

    
    