import tkinter as tk
import random
import string

def generate_password():
    length = int(entry_length.get())  # Get password length from input field
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    label_result.config(text=f"Generated Password: {password}")

root = tk.Tk()
root.title("Random Password Generator")
label_instructions = tk.Label(root, text="Enter password length:")
label_instructions.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.grid(row=1, column=0, columnspan=2, pady=20)
label_result = tk.Label(root, text="Generated Password: ")
label_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()