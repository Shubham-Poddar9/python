import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    result = determine_winner(user_choice, computer_choice)
    
    player_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=f"Result: {result}")

def reset_game():
    player_choice_label.config(text="Your choice: ")
    computer_choice_label.config(text="Computer's choice: ")
    result_label.config(text="Result: ")

root = tk.Tk()
root.title("Rock Paper Scissors")

rock_button = tk.Button(root, text="Rock", width=20, command=lambda: play_game("Rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", width=20, command=lambda: play_game("Paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", width=20, command=lambda: play_game("Scissors"))
scissors_button.pack(pady=10)

player_choice_label = tk.Label(root, text="Your choice: ", font=("Arial", 14))
player_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer's choice: ", font=("Arial", 14))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=20)

reset_button = tk.Button(root, text="Reset", width=20, command=reset_game)
reset_button.pack(pady=10)
root.mainloop()
