a=float(input("Enter student's marks"))
b=float(input(""))
c=float(input(""))
d=float(input(""))
e=float(input(""))
z=float(input("Enter total marks"))
p1=(a*100)/z
p2=(b*100)/z
p3=(c*100)/z
p4=(d*100)/z
p5=(e*100)/z
Total_percentage=(a+b+c+d+e)*100/(5*z)
print(f"The subject wise percentages are as follow:{p1},{p2},{p3},{p4},{p5}")
print(f"The total percentage of the student is{Total_percentage}")


