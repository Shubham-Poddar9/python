a=int(input("Enter the number"))
b=int(input("Enter number"))

c=set()
d=set()

for i in range(1,a+1):
    if a%i==0:
        c.add(i)

for j in range(1,b+1):
    if b%j==0:
        d.add(j)
print(c)
print(d)
print(max(c.intersection(d)))
