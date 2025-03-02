a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
lcm = max(a, b)
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1  
print(f"LCM of {a} and {b} is {lcm}")