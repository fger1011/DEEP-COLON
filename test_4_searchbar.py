import tkinter as tk
import pymongo
from tkinter import ttk
from pymongo import MongoClient

# Define function to handle search button click
def search_users():
    # Clear any previous search results
    search_results.delete(0, tk.END)

    # Get search term from input box
    search_term = search_input.get()

    # Connect to MongoDB and perform search
    client = MongoClient('<mongodb_connection_string>')
    db = client['mydatabase']
    collection = db['registration2']

    results = collection.find({"lastname": {"$regex": search_term, "$options": "i"}})

    if results.count() > 0:
        # Display search results
        for result in results:
            search_results.insert(tk.END, f"Name: {result['firstname']} {result['lastname']}  Birthday: {result['birthday']}   Age: {result['age']}   Sex: {result['sex']}   Address: {result['address']}   Contact Number: {result['contact_number']}  Emergency Contact Number: {result['emergency_contact_number']}  Emergency Contact Name: {result['emergency_contact_name']} Marital Status: {result['marital_status']}")
    else:
        # Display message if no results found
        search_results.insert(tk.END, "No results found.")

    client.close()

# Create GUI window
window = tk.Tk()
window.title('User Search')
window.geometry('700x500')
window.config(bg="#2c3e50")  # Navy blue background color

window.state('zoomed')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (600 // 2)
y = (screen_height // 2) - (600 // 2)
window.geometry(f'+{x}+{y}')

# Define styles
style = ttk.Style(window)
style.theme_use('clam')
style.configure('TLabel', font=('Arial', 12), foreground="#000000")  
style.configure('TEntry', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12), foreground="#000000", background="#2980b9")  

# Add search elements
search_label = ttk.Label(window, text='Search for user by last name:', foreground="#000000")  
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
