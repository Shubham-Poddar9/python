def time(n):
    iteration=0
    print("the value of n is this",n)
    iteration=iteration+1
    print(iteration)
time(4)
time(9)
time(5)
print("iterations are not dependent on n")
def ontime(n):
    iteration=0
    for i in range(1,n+1):
        iteration=iteration+1
    print("when the value of n is this ",n,"The iteration is this",iteration)
ontime(20)
ontime(10)
ontime(31)
print("iterations are dependent on n")

def time1(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("$",end="")
            iteration=iteration+1
        print()
    print("when the value is this",n,"The iteration",iteration)
time1(3)
time1(1)
time1(5)
print("iterations are square of value of n")