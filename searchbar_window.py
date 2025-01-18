import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Define function to handle search button click
def search_users():
    # Clear any previous search results
    search_results.delete(0, tk.END)

    # Get search term from input box
    search_term = search_input.get()

    # Connect to database and perform search
    conn = sqlite3.connect('registration.db')
    cursor = conn.cursor()
    cursor.execute("SELECT firstname, lastname, birthday, age, sex, address, contact_number, emergency_contact_name, emergency_contact_number, marital_status FROM registration2 WHERE lastname LIKE '%' || ? || '%'", (search_term,))

    results = cursor.fetchall()

    if results:
        # Display search results
        for result in results:
            search_results.insert(tk.END, f"Name:{result[0]} {result[1]}  Birthday: {result[2]}   Age: {result[3]}   Sex: {result[4]}   Address: {result[5]}   Contact Number: {result[6]}  Emergency Contact Number: {result[6]}  Emergency Contact Name: {result[7]} Marital Status: {result[8]}")
    else:
        # Display message if no results found
        search_results.insert(tk.END, "No results found.")

    conn.close()

# Create GUI window
window = tk.Tk()
window.title('User Search')
window.geometry('700x500')
window.config(bg="#2196f3")  # Vibrant blue background color

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (600 // 2)
y = (screen_height // 2) - (600 // 2)
window.geometry(f'+{x}+{y}')

# Define styles
style = ttk.Style(window)
style.theme_use('clam')
style.configure('TLabel', font=('verdana', 12), foreground="#ffffff")  # White label text color
style.configure('TEntry', font=('verdana', 12))
style.configure('TButton', font=('verdana', 12), foreground="#ffffff", background="#4caf50")  # Green search button

# Add search elements
search_label = ttk.Label(window, text='Search for user by last name:', foreground="#000000")  # White label text color
search_label.pack(pady=10)

search_input = ttk.Entry(window, width=30)
search_input.pack()

search_button = ttk.Button(window, text='Search', command=search_users, style='TButton', width=15)
search_button.pack(pady=10)

search_results = tk.Listbox(window, width=100, height=30, font=('Arial', 12))
search_results.pack()

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# Start GUI loop
window.mainloop()
