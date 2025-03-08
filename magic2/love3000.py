a=int(input("enter number"))
s=int(input("enter another number"))

for i in range(a,s+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)