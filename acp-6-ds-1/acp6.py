def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_two_digit_primes():
    for i in range(10, 100):
        if is_prime(i):
            print(i)

find_two_digit_primes()
