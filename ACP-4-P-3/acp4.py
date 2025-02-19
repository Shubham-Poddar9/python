import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Grid Layout")

# Create Labels and Entry widgets
label_name = tk.Label(root, text="Name:")
label_age = tk.Label(root, text="Age:")
label_email = tk.Label(root, text="Email:")

entry_name = tk.Entry(root)
entry_age = tk.Entry(root)
entry_email = tk.Entry(root)

# Create buttons
button_submit = tk.Button(root, text="Submit")
button_reset = tk.Button(root, text="Reset")

# Using grid to arrange widgets
label_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
name.grid(row=0, column=1, padx=10, pady=10)

label_age.grid(row=1, column=0, padx=10, pady=10, sticky="w")
age.grid(row=1, column=1, padx=10, pady=10)

email.grid(row=2, column=0, padx=10, pady=10, sticky="w")
email.grid(row=2, column=1, padx=10, pady=10)


root.mainloop()
