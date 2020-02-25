def hcf(x,y):
    if(x>y):
        smaller=x
    else:
        smaller=y
    for i in range(1,smaller+1):
        if(x%i==0) and(y%i==0):
            hcf=i
    return hcf
x=int(input("Enter the number"))
y=int(input("Enter the number"))
print("Lcm is",hcf(x,y))
