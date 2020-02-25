a=int(input("Entee the number"))
if a>1:
    for i in range(2,a):
        if(a%i)==0:
            print("{} is Not a prime numebr".format(a))
            break
    else:
         print("{} is a prime number".format(a))
else:
    print("{} is Not a prime number".format(a))