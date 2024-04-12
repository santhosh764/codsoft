import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_button_clicked():
    length = length_entry.get()
    try:
        length = int(length)
        if length <= 0:
            raise ValueError
        password = generate_password(length)
        password_display.config(state='normal')
        password_display.delete(1.0, tk.END)
        password_display.insert(tk.END, password)
        password_display.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for the password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and pack the widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_button_clicked)
generate_button.pack()

password_display = tk.Text(root, height=5, width=40)
password_display.pack()

password_display.config(state='disabled')

# Run the main event loop
root.mainloop()