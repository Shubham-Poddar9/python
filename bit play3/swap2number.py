def swap(a, b):
    a=a^b
    b=a^b
    a=a^b
    print("after swap the values are this",a,b)
swap(3,17)
def swap2(a, b):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print ("After Swapping: a = ", a, " b =", b)
swap2(31,2)