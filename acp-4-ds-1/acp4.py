def binary_to_decimal(binary):
    decimal = int(binary, 2)  
    return decimal

def decimal_to_binary(decimal):
    binary = bin(decimal)[2:] 
    return binary
choice = input("Choose conversion: \n1. Binary to Decimal \n2. Decimal to Binary\nEnter 1 or 2: ")
if choice == '1':
    binary_num = input("Enter a binary number: ")
    print(f"Decimal Equivalent: {binary_to_decimal(binary_num)}")
elif choice == '2':
    decimal_num = int(input("Enter a decimal number: "))
    print(f"Binary Equivalent: {decimal_to_binary(decimal_num)}")
else:
    print("Invalid choice! Please enter 1 or 2.")
