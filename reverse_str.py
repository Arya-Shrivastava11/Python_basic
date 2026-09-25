str1="Today was a good day"
n=len(str1)
list1=[]
for i in range(n,-1,-1):#In reverse python slicing if the last element is 0 it prints blank.
#we are using conditional statements and a very interesting [0::-1] because leaving the stop
#place blank just makes it safely grab the 0th element.
    if i==0:
        a=str1[0::-1]
    else:
        a=str1[i:i-1:-1]

    list1.append(a)
str2=''.join(list1)
print(str2)

    
    
