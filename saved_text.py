import tkinter as tk

def save_text():
    text = text_widget.get("1.0", "end-1c")  # Get the text from the Text widget
    with open("saved_text.txt", "w") as file:
        file.write(text)

def fetch_saved_text():
    try:
        with open("saved_text.txt", "r") as file:
            saved_text = file.read()
            text_widget.delete("1.0", "end")  # Clear the existing text in the Text widget
            text_widget.insert("1.0", saved_text)  # Insert the saved text
    except FileNotFoundError:
        # Handle the case when the file is not found
        pass

# Create the tkinter window
window = tk.Tk()



# Create a Text widget
text_widget = tk.Text(window, height=10, width=30)
text_widget.pack()

# Create buttons for saving and fetching the text
save_button = tk.Button(window, text="Save Text", command=save_text)
save_button.pack()

fetch_button = tk.Button(window, text="Fetch Saved Text", command=fetch_saved_text)
fetch_button.pack()

# Start the tkinter event loop
window.mainloop()
