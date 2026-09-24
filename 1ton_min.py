N=int(input("Enter the no. of inputs"))
list1=[]
for i in range(1,N+1):
    a=float(input(f"Enter input{i}"))
    list1.append(a)
print(min(list1))
