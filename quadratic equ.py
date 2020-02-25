import cmath
a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Rnter the number"))
d=(b**2)-(4*a*c)
m=(-b-cmath.sqrt(d))/(2*a)
n=(-b+cmath.sqrt(d))/(2*a)
print("the solution is {0} and{1}".format(m,n))