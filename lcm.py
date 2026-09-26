a=int(input("Enter number1"))
b=int(input("Enter number2"))
list1=[]
for i in range(1,(a*b)+1):
    if i%a==0 and i%b==0:
        list1.append(i)
print(list1[0])