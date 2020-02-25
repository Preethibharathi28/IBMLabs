a=int(input("Enter the number"))
if(a % 4) == 0:
    if(a % 100) == 0:
        if(a % 400) == 0:
            print("{} is a leap year".format(a))
        else:
            print("{} is not a leap year".format(a))
    else:
        print("{} is a leap year".format(a) )
else:19
    print("{} is  not  a leap year".format(a))