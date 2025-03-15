def bit(n):
    ones=0
    zeros=0
    while n:
        if n&1==1:
            ones+=1
        else:
            zeros+=1
        n>>=1
    print("The total no of ones are ",ones)
    print("the total no of zeros are",zeros)
n=int(input("enter number"))
bit(n)