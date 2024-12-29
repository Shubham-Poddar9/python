w=int(input("Enter the number"))
for i in range(2,w):
    if w%i==0:
        print("The number is not a prime number",w)

        break
else:
    print(" your number is prime number")