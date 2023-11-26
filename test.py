import tkinter as tk
import webbrowser

def open_facebook_page():
    webbrowser.open('https://www.newsinaimdi.com/public/index.php')  # Replace with the desired Facebook page URL

root = tk.Tk()

# Load the logo image
logo_image = tk.PhotoImage(file=r'C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\logo.png')  # Replace with the path to your logo image

# Create a label with the logo image
logo_label = tk.Label(root, image=logo_image)

# Configure the label to respond to mouse clicks
logo_label.bind("<Button-1>", lambda e: open_facebook_page())

# Pack the label into the root window
logo_label.pack()

root.mainloop()
