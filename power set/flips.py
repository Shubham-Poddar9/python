def flips(n1,n2):
    flip=0
    while n1>0 or n2>0:
        t1=n1&1
        t2=n2&1
        if t1 !=t2:
            flip=flip+1
        n1>>=1
        n2>>=1
    return flip
a=int(input("enter no"))
b=int(input("enter another no"))
print(flips(a,b))