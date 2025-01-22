def check_armstrong_number(number):
    num_str = str(number)
    
    num_digits = len(num_str)
    
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_digits
    
    if sum == number:
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")

number = int(input("Enter a number: "))
check_armstrong_number(number)
