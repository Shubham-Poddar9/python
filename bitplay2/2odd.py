def odd(arr,size):
    res=arr[0]
    x=0
    y=0
    for i in range(1,size):
        res=res^arr[i]
    setbit=res & ~ (res-1)
    for i in range(size):
        if arr [i]&setbit:
            x=x^arr[i]
        else:
            y=y^arr[i]
    print("the result is this",x,y)
arr=[1,5,5,7,7,8,9,9]
odd(arr,len(arr))