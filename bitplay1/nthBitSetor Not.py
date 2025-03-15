def bit1(number,n):
    if number&(1<<n-1):
        print("Set")
    else:
        print("notset")
a=int(input("Enter the number"))
b=int(input("enter the bit"))
bit1(a,b)