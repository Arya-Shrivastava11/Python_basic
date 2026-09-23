a = float(input("Enter numbers"))
b = float(input(""))
c = float(input(""))

if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c

print(f"The largest number is: {largest}")