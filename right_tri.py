N=int(input("Enter Dimension"))
for i in range(N+1,1,-1):
    for j in range(1,N+1):
        if j>=i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
            
    
