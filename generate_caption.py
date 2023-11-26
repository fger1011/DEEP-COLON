import tkinter as tk
from PIL import ImageTk, Image
import torch
import torchvision.transforms as transforms
from model import CNNtoRNN
from get_loader import Vocabulary

# Create a Tkinter window
window = tk.Tk()

# Set the window title
window.title("Image Captioning")

# Create a label to display the image
image_label = tk.Label(window)
image_label.pack()

# Create a label to display the caption
caption_label = tk.Label(window, font=("Helvetica", 14))
caption_label.pack()

# Load the vocabulary
vocab = Vocabulary.load_vocab("vocab.json")

# Define the hyperparameters
embed_size = 256
hidden_size = 256
num_layers = 1

# Calculate the vocabulary size based on the dataset
vocab_size = len(vocab)

# Define the model architecture
model = CNNtoRNN(embed_size, hidden_size, vocab_size, num_layers)

# Load the trained model checkpoint
checkpoint = torch.load("my_checkpoint.pth")

# Update the model's state dictionary to match the checkpoint
model_dict = model.state_dict()
checkpoint_dict = checkpoint["state_dict"]

# Remove the incompatible keys from the checkpoint
checkpoint_dict = {k: v for k, v in checkpoint_dict.items() if k in model_dict}

# Load the updated state dictionary into the model
model_dict.update(checkpoint_dict)
model.load_state_dict(model_dict)

model.eval()

# Define the image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Function to update the image and caption
def update_image_caption(image_path):
    # Open and transform the image
    image = Image.open(image_path)
    image = transform(image).unsqueeze(0)

    # Generate the caption using the model
    with torch.no_grad():
        caption = model.caption_image(image, vocab)

    # Convert the caption from a list of tokens to a string
    caption_text = " ".join(caption)

    # Update the image label
    photo = ImageTk.PhotoImage(Image.open(image_path))
    image_label.configure(image=photo)
    image_label.image = photo

    # Update the caption label
    caption_label.configure(text=caption_text)

# Example usage
image_path = "test_examples/colon_4.jpg"
update_image_caption(image_path)

# Start the Tkinter event loop
window.mainloop()
