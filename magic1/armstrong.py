number=int(input("Enter your number"))
tem=number
result=0
while tem>0:
    dg=tem%10
    result=result+dg**3
    tem=tem//10
if number==result:
    print("its an armstrong number")
else:
    print("it is not armstrong number")