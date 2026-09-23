n=int(input("Enter a number"))
list1=[]
for i in range(1,n+1):
    if n%i==0:
        list1.append(i)
if len(list1)==2:
    print("Number is prime")
else:
    print("Number is not prime")
