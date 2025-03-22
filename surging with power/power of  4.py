a=int(input("enter the number"))
if a&(a-1)==0:
    if a==1:
        print("its power of 4")
        exit()
    elif a%10==4 or  a%10==6:
        print("its power of 4")
    else:
        print("its not power of 4")
else:
    print("its not power of 4")
    