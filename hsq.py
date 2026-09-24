S=int(input("Enter dimensions"))
for i in range(1,S+1):
    for j in range(1,S+1):
        if j==1 or i==1 or j==S or i==S:
            print('*  ',end="")
        else:
            print("   ",end="")
        
    print()
   