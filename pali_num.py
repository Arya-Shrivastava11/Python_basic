n=int(input("Enter a number"))
copy=n
str1=str(copy)
list1=[]
rem=0
q=0
rev=0
while(copy!=0):
    rem=copy%10
    list1.append(rem)
    q=copy//10
    copy=q
for i in list1:
    rev=rev*10+i
if rev==n:
    print("No. is a palindrome")
else:
    print("No. is not a palindrome")


