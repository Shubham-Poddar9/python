def power(a,b):
    result=1
    while b>0:
        if b%2==0:
            a=a*a
            b>>=1
        else:
            result=result*a
            b=b-1
    return result
x=int(input("enter the number"))
y=int(input("enter other number"))
print(power(x,y))