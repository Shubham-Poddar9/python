def algo(n):
    return n*(n+1)//2
print(algo(3))  
#total no of iterations are 1
def algo1(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print(sum)
algo1(3)
#total no of iterations are 3
def algo2(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum=sum+1
    print(sum)
algo2(3)
#total no of iterations are 6