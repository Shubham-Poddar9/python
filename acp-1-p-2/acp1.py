import random

def guess_number():
    random_number = random.randint(1, 100)  
    attempts = 0

    print("Welcome to the Guess the Number Game!")
    print("Guess a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the right number {random_number} in {attempts} attempts.")
            break

guess_number()
