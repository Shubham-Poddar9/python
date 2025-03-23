a=int(input("ENter larger number"))
b=int(input("enter smaler number"))
q=0
if b==0:
    print("division not possible")
    exit()
else:
    while a>=b:
        a=a-b
        q=q+1
    print(q)