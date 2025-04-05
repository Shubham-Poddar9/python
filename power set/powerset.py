def a(set1,size):
    power1=2**size
    outer=0
    inner=0
    for outer in range(0,power1):
        for inner in range(0,size):
            if outer & (1<<inner)>0:
                print(set1[inner],end="")
        print()
set1=[1,7,17]
size=len(set1)
a(set1,size)