a = int(input("Enter the number: "))
if a & (a - 1) == 0:  
    while a % 8 == 0 and a > 0: 
        a //= 8
    if a == 1: 
        print("It's a power of 8")
    else:
        print("It's not a power of 8")
else:
    print("It's not a power of 8")
