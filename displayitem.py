n=int(input("Enter no. strings and no's items in a list"))
list1=[]
for i in range(1,n+1):
    a=input(f"Enter item{i}")
    list1.append(a)
for item in list1:
    print(item)
