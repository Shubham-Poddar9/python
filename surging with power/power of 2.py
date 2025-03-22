ans=0
a=0
b=int(input("enter the number"))
while ans<b:
    ans=1<<a
    if ans==b:
        print("its a power of two")
        break
    a+=1
else:
   print("its not a power")
