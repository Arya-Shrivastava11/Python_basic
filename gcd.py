a=int(input("Enter number1"))
b=int(input("Enter number2"))
list1=[]
if a>b:
    for i in range(1,b+1):
        if a%i==0 and b%i==0:
            list1.append(i)
else:
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            list1.append(i)
print(list1[-1])