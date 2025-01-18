from tkinter import *
from tkinter import filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip

def browse_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Video files", ".mp4"), ("all files", ".*")))
    video_clip = VideoFileClip(filename)
    player = Label(right_frame, text="Playing video...")
    player.pack()
    video_clip.preview()

root = Tk()  # create root window
root.title("Basic GUI Layout")  # title of the GUI window
root.geometry("1500x800")  # specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color

# Create left and right frames
left_frame = Frame(root, width=200, height=800, bg='grey')
left_frame.grid(row=0, column=10, padx=200, pady=5)

right_frame = Frame(root, width=850, height=600, bg='grey')
right_frame.grid(row=0, column=1, padx=30, pady=30)

# Create frames and labels in left_frame

# Add button to browse video file
upload_button = Button(left_frame, text="Upload Video", command=browse_file)
upload_button.pack(pady=20)

root.mainloop()