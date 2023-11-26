import tkinter as tk
from PIL import Image, ImageTk
import webbrowser


def register_patient():
    window.destroy()  # Close the main window
    import register_window

def search_patient():
    window.destroy()  # Close the main window
    import searchbar_window

def on_button1_enter(event):
    register_button.config(bg="khaki")

def on_button1_leave(event):
    register_button.config(bg="SystemButtonFace")

def on_button2_enter(event):
    search_button.config(bg="khaki")

def on_button2_leave(event):
    search_button.config(bg="SystemButtonFace")

def open_website_page():
    webbrowser.open('https://www.newsinaimdi.com/public/index.php')  # Replace with the desired Facebook page URL


def resize_image():
    # Get the size of the screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Resize the image to fit the screen
    resized_image = original_image.resize((screen_width, screen_height))

    # Decrease the opacity of the image
    resized_image = resized_image.convert("RGBA")
    data = resized_image.getdata()

    new_data = []
    for item in data:
        # Set the alpha value to 50% (128 out of 255)
        new_data.append((item[0], item[1], item[2], 128))

    resized_image.putdata(new_data)

    # Convert the resized image to Tkinter-compatible format
    image_tk = ImageTk.PhotoImage(resized_image)

    # Update the image displayed in the label
    label.config(image=image_tk)
    label.image = image_tk  # Keep a reference to the resized image
    
# Create the main window
window = tk.Tk()
window.title("DEEP-COLON")
window.geometry('700x500')


window.state('zoomed')


original_image = Image.open(r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\mdi.jpg")
deep_image = Image.open(r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\deep-colon-removebg-preview.png")
deep_photo = ImageTk.PhotoImage(deep_image)
logo_image = Image.open(r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\logo.png")
logo_photo = ImageTk.PhotoImage(logo_image)

label = tk.Label(window)
label.pack(fill=tk.BOTH, expand=True)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (600 // 2)
y = (screen_height // 2) - (600 // 2)
window.geometry(f'+{x}+{y}')

# Call the resize_image function to resize the image to fit the full screen
resize_image()

image = tk.PhotoImage(file=r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\register (4).png")
image2 = tk.PhotoImage(file=r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\search.png")


# Create and configure the labels and buttons
register_button = tk.Button(window, text="Register Patient",image=image, font=("Lexend", 16), width=290, height=100, command=register_patient)
register_button.place(relx=0.3, rely=0.5, anchor="center")

search_button = tk.Button(window, text="Search Patient", image=image2, font=("Lexend", 16), width=290, height=100, command=search_patient)
search_button.place(relx=0.7, rely=0.5, anchor="center")

register_button.bind("<Enter>", on_button1_enter)
register_button.bind("<Leave>", on_button1_leave)

search_button.bind("<Enter>", on_button2_enter)
search_button.bind("<Leave>", on_button2_leave)

logo_label = tk.Label(window, image=logo_photo)
logo_label.place(x=100, y=100)

logo_label.bind("<Button-1>", lambda e: open_website_page())

deep_label = tk.Label(window, image=deep_photo)
deep_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)


window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# Start the main event loop
window.mainloop()
