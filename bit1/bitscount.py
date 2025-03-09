def number(n):
    count=0
    while n:
        count=count+1
        n>>=1
    print(count)
a=int(input("enter the number"))
number(a)