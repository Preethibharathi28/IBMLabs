def lcm(x,y):
    if(x>y):
        greater=x
    else:
        greater=y
    while(True):
        if((greater%x==0)and(greater%y==0)):
            lcm=greater
            break
        greater += 1
    return lcm
x=int(input("Enter the number"))
y=int(input("Enter the number"))
print("Lcm is",lcm(x,y))


