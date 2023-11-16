import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorAppforCodSoft:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator for CodSoft")
        self.master.geometry("400x250")

        # Set background color for the main window
        self.master.configure(bg="#e0e0e0")

        # Labels and Entry for Username
        self.username_label = tk.Label(master, text="Username:", bg="#e0e0e0")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)

        self.username_entry = tk.Entry(master)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Labels and Entry for Password Length
        self.length_label = tk.Label(master, text="Password Length:", bg="#e0e0e0")
        self.length_label.grid(row=1, column=0, padx=10, pady=10)

        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=1, column=1, padx=10, pady=10)

        # Button to generate password
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Display generated password
        self.password_label = tk.Label(master, text="Generated Password:", bg="#e0e0e0")
        self.password_label.grid(row=3, column=0, padx=10, pady=10)

        self.password_display = tk.Entry(master, state="readonly")
        self.password_display.grid(row=3, column=1, padx=10, pady=10)

        # Accept and Reset Buttons
        self.accept_button = tk.Button(master, text="Accept", command=self.accept_password)
        self.accept_button.grid(row=4, column=0, pady=10)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_inputs)
        self.reset_button.grid(row=4, column=1, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Password length must be greater than 0.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            return

        password = self.generate_random_password(length)
        self.password_display.config(state="normal")
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)
        self.password_display.config(state="readonly")

    def generate_random_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def accept_password(self):
        username = self.username_entry.get()
        password = self.password_display.get()

        if not username or not password:
            messagebox.showwarning("Warning", "Please generate a password before accepting.")
            return

        messagebox.showinfo("Accepted", f"Username: {username}\nPassword: {password} \nPassword has been accepted.")

    def reset_inputs(self):
        self.username_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.password_display.config(state="normal")
        self.password_display.delete(0, tk.END)
        self.password_display.config(state="readonly")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorAppforCodSoft(root)
    root.mainloop()
