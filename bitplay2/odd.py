def odd(arr):
    res=0
    for i in arr:
        res=res^i
    print("the result is this",res)
arr=[5,5,7,7,8,9,9]
odd(arr)