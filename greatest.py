a = float(input("Enter the number"))
b = float(input("Enter the number"))
c = float(input("Enter the number"))
if (a>=b) and (a>=c):
    large = a
elif (b>=a) and (b>=c):
    large = b
else:
    large = c
print("The large number is",large)

