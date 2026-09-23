a=float(input("Enter a number"))
b=float(input("Enter next number"))
c=input("Enter operation")
if c=='+':
    print(f"Addtion=",a+b)
elif c=='-':
    print(f"Substraction=",a-b)
elif c=='*':
    print(f"Multiplication=",a*b)
elif c=='/':
    print(f"Division =",a/b)
elif c=='^':
    print(f"a^b=", a**b)
elif c=='%':
    print(f"Remainder=",a%b)
else:
    print("Invalid Operation")


