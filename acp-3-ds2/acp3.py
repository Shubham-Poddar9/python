def reverse_bits(num):
    reversed_num = 0
    bit_count = 32 

    for i in range(bit_count):
        reversed_num <<= 1  
        reversed_num |= (num & 1) 
        num >>= 1  

    return reversed_num

number = int(input("Enter a number: "))  
print("Original Number:", number)
reversed_number = reverse_bits(number)
print("Reversed Bits:", reversed_number)  
