import json
import tkinter as tk
from tkinter import messagebox

# Load existing birthdays
def load_birthdays():
    try:
        with open("birthdays.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save new birthday
def save_birthday():
    name = name_entry.get()
    date = date_entry.get()

    if name and date:
        birthdays = load_birthdays()
        birthdays[name] = date

        with open("birthdays.json", "w") as file:
            json.dump(birthdays, file, indent=4)

        messagebox.showinfo("Success", f"Birthday of {name} saved!")
        root.destroy()
    else:
        messagebox.showerror("Error", "Please enter all fields!")

# GUI Setup
root = tk.Tk()
root.title("Add Birthday")
root.geometry("300x200")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Date (MM-DD):").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Button(root, text="Save Birthday", command=save_birthday).pack()
root.mainloop()
