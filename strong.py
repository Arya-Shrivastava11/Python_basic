n=int(input("Enter a number"))
copy=n
rem=0
q=0
sum1=0

while(copy!=0):
    f=1
    rem=copy%10
    for i in range(1,rem+1):
        
        f=f*i
    sum1=sum1+f
    q=copy//10
    copy=q
if sum1==n:
    print("No. is strong")
else:
    print("No is not strong")
    
