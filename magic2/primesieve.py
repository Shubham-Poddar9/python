a=[2,3,6,8,9,777,88,96,3159,2887,2897,2903,2909]
for i in a:
    for j in range(2,i):
        if i%j==0:
           break
    else:
        print(i)