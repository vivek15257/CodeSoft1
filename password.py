import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    char_pool = ""
    
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation
    
    if not char_pool:
        raise ValueError("No character types selected! Please select at least one character type.")
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# Function to handle the password generation process
def generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()
        
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Create the main window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")  # Set the size of the window

# Create and place the GUI elements
tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

uppercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, column=0, columnspan=2, sticky=tk.W, padx=10, pady=5)

lowercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var).grid(row=2, column=0, columnspan=2, sticky=tk.W, padx=10, pady=5)

digits_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=3, column=0, columnspan=2, sticky=tk.W, padx=10, pady=5)

special_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=4, column=0, columnspan=2, sticky=tk.W, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate, bg="blue", fg="white")
generate_button.grid(row=5, column=0, columnspan=2, pady=20)

tk.Label(root, text="Generated Password:").grid(row=6, column=0, sticky=tk.W, padx=10)
result_entry = tk.Entry(root, width=50)
result_entry.grid(row=6, column=1, padx=10, pady=5)

# Start the GUI event loop
root.mainloop()
