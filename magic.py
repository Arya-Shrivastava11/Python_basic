n=int(input("Enter a number:"))
copy=n
rem=0
qoutient=0

sum2=10
while(sum2>=10):
    while(copy!=0):
        sum1=0   
        rem=copy%10
        qoutient=copy//10
        copy=qoutient
        sum1=sum1+rem
    sum2=sum1
    copy=sum2
if copy==1:
    print("no. is magic")
else:
    print("no is not magic")



