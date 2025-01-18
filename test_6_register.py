import tkinter as tk
import tkcalendar
import pymongo
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Access the database and create a collection if it doesn't exist
db = client["registration2"]
collection = db["patients"]

def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # Personal info
        firstname = firstname_entry.get()
        lastname = lastname_entry.get()
        birthday = birthday_entry.get()
        age = age_entry.get()
        sex = sex_combobox.get()

        # Contact info
        address = address_entry.get()
        contact_number = contact_number_entry.get()
        emergency_contact_name = emergency_contact_name_entry.get()
        emergency_contact_number = emergency_contact_number_entry.get()
        marital_status = marital_status_combobox.get()

        if firstname and lastname and birthday and age and sex and address and contact_number and emergency_contact_name and emergency_contact_number and marital_status:
            # Insert data into the collection
            user_data = {
                "firstname": firstname,
                "lastname": lastname,
                "birthday": birthday,
                "age": int(age),
                "sex": sex,
                "address": address,
                "contact_number": contact_number,
                "emergency_contact_name": emergency_contact_name,
                "emergency_contact_number": emergency_contact_number,
                "marital_status": marital_status
            }
            collection.insert_one(user_data)

            # Display success message
            messagebox.showinfo(title="Success", message="Data entered successfully!")

            window.destroy()
            import home_window

        else:
            # Display error message if any field is blank
            messagebox.showerror(title="Error", message="Please fill up all fields.")
    else:
        # Display error message if user has not accepted terms and conditions
        messagebox.showerror(title="Error", message="You must accept the terms and conditions to continue.")

window = tk.Tk()
window.title("Data Entry Form")
window.geometry('700x600')
window.config(bg="#2c3e50")

window.state('zoomed')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (600 // 2)
y = (screen_height // 2) - (600 // 2)
window.geometry(f'+{x}+{y}')

def back_home():
    window.withdraw()
    window.destroy()
    import test_3_home_window

frame = tk.Frame(window, bg="#2c3e50")
frame.pack()

# Personal Information Frame
personal_info_frame = tk.LabelFrame(frame, text="Personal Information", bg="#2c3e50", fg="#ffffff")
personal_info_frame.pack(padx=10, pady=10, fill="both", expand=True)

firstname_label = tk.Label(personal_info_frame, text="First Name:", font=("Arial", 12), bg="#2c3e50", fg="#ffffff")
firstname_label.grid(row=0, column=0, sticky="e")
firstname_entry = tk.Entry(personal_info_frame, width=30)
firstname_entry.grid(row=0, column=1)

lastname_label = tk.Label(personal_info_frame, text="Last Name:", font=("Arial", 12), bg="#2c3e50", fg="#ffffff")
lastname_label.grid(row=1, column=0, sticky="e")
lastname_entry = tk.Entry(personal_info_frame, width=30)
lastname_entry.grid(row=1, column=1)

birthday_label = tk.Label(personal_info_frame, text="Birthday:", font=("Arial", 12), bg="#2c3e50", fg="#ffffff")
birthday_label.grid(row=2, column=0, sticky="e")
birthday_entry = tkcalendar.DateEntry(personal_info_frame, date_pattern='yyyy-mm-dd')
birthday_entry.grid(row=2, column=1)

age_label = tk.Label(personal_info_frame, text="Age:", font=("Arial", 12), bg="#2c3e50", fg="#ffffff")
age_label.grid(row=3, column=0, sticky="e")
age_entry = tk.Entry(personal_info_frame, width=30)
age_entry.grid(row=3, column=1)

sex_label = tk.Label(personal_info_frame, text="Sex:", font=("Arial", 12), bg="#2c3e50", fg="#ffffff")
sex_label.grid(row=4, column=0, sticky="e")
sex_combobox = ttk.Combobox(personal_info_frame, values=["Male", "Female"])
sex_combobox.grid(row=4, column=1)

# Contact Information Frame
contact_info_frame = tk.LabelFrame(frame, text="Contact Information", bg="#2c3e50", fg="#ffffff")
contact_info_frame.pack(padx=10, pady=10, fill="both", expand=True)

address_label = tk.Label(contact_info_frame, text="Address:", font=("Arial", 12), bg="#2c3e50", fg="#ffffff")
address_label.grid(row=0, column=0, sticky="e")
address_entry = tk.Entry(contact_info_frame, width=30)
address_entry.grid(row=0, column=1)

contact_number_label = tk.Label(contact_info_frame, text="Contact Number:", font=("Arial", 12), bg="#2c3e50", fg="#ffffff")
contact_number_label.grid(row=1, column=0, sticky="e")
contact_number_entry = tk.Entry(contact_info_frame, width=30)
contact_number_entry.grid(row=1, column=1)

emergency_contact_name_label = tk.Label(contact_info_frame, text="Emergency Contact Name:", font=("Arial", 12), bg="#2c3e50", fg="#ffffff")
emergency_contact_name_label.grid(row=2, column=0, sticky="e")
emergency_contact_name_entry = tk.Entry(contact_info_frame, width=30)
emergency_contact_name_entry.grid(row=2, column=1)

emergency_contact_number_label = tk.Label(contact_info_frame, text="Emergency Contact Number:", font=("Arial", 12), bg="#2c3e50", fg="#ffffff")
emergency_contact_number_label.grid(row=3, column=0, sticky="e")
emergency_contact_number_entry = tk.Entry(contact_info_frame, width=30)
emergency_contact_number_entry.grid(row=3, column=1)

marital_status_label = tk.Label(contact_info_frame, text="Marital Status:", font=("Arial", 12), bg="#2c3e50", fg="#ffffff")
marital_status_label.grid(row=4, column=0, sticky="e")
marital_status_combobox = ttk.Combobox(contact_info_frame, values=["Single", "Married", "Divorced", "Widowed"])
marital_status_combobox.grid(row=4, column=1)

# Accept Terms Frame
terms_frame = tk.LabelFrame(frame, text="Terms & Conditions", bg="#2c3e50", fg="#ffffff")
terms_frame.pack(padx=10, pady=10, fill="both", expand=True)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted", bg="#fff")
terms_check.pack()

# Submit Button
button = tk.Button(frame, text="Submit", command=enter_data, bg="#2980b9", fg="#ffffff")
button.pack(padx=10, pady=10)

# Back button
back_button = ttk.Button(frame, text="Back", command=back_home)
back_button.pack(padx=10, pady=10)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()
