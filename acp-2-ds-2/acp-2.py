def rightmost_set_bit(n):
    return n & -n

number = 18 
print(f"Rightmost set bit of {number} is {rightmost_set_bit(number)}") 
