a = input("Enter the character")
a = a.casefold()
b = reversed(a)
print()
if list(a) == list(b):
    print("The string is a palindrom")
else:
    print("The string is not a palindrom")
