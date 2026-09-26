n=int(input("Enter the number:"))
rem=0
count=0
while n!=0:
    rem=n%10
    n=n//10
    count+=1
print(count)

    