list1=[1,5,3,9,20,56,12,2]
newlist=[]
for item in list1:  
    if item%2==0:
        newlist.append(item)
    
print(len(newlist))