def longest_consecutive_ones(n):
    binary_str = bin(n)[2:]
    
    bits = list(binary_str)  # ['1', '0', '1', '1', '1', ...]
    
    max_count = 0
    current_count = 0
    
    for bit in bits:
        if bit == '1':
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    
    return max_count

num = int(input("Enter a number: "))
print("Longest consecutive 1's:", longest_consecutive_ones(num))
