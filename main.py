import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import cv2
from PIL import ImageTk, Image
from tensorflow.python.saved_model import tag_constants
# Global variables
is_playing = False
current_frame = None
video_path = None
processed_video_path = None
cap = None

def open_file():
    global video_path
    video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    if video_path:
        process_video(video_path)

def process_video(video_path):
    global processed_video_path
    # Define the output video path
    output_dir = "./outputs"
    os.makedirs(output_dir, exist_ok=True)
    processed_video_path = os.path.join(output_dir, "processed_video.mp4")

    # Show the "Processing" label
    loading_label.config(text="Processing...")

    # Run the object_tracker.py script as a subprocess, passing the video path and output video path as arguments

    #command = ['python', 'object_tracker.py', '--video', video_path, '--output', processed_video_path, '--model', 'yolov4']
    #subprocess.run(command)

    #os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # Replace '0' with the GPU device index you want to use
    # Path to the save_model.py script
    save_model_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject17\AiM\save_model.py"

    # Path to the weights file
    weights_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject17\AiM\data\yolov4.weights"

    # Command to run the save_model.py script
    command = [
        'python',
        save_model_path,
        '--weights', weights_path,
        '--output', './checkpoints/yolov4-tiny-416',
        '--model', 'yolov4',
        '--tiny'
    ]

    # Execute the command to run the save_model.py script
    subprocess.run(command)


    command = ['python', 'object_tracker.py', '--video', video_path, '--output', processed_video_path, '--weights', './checkpoints/yolov4-tiny-416', '--model', 'yolov4']

    subprocess.run(command)

    # Hide the "Processing" label
    loading_label.config(text="")

    # Play the processed video
    play_video(processed_video_path)

def play_video(video_path):
    global is_playing, current_frame, cap
    cap = cv2.VideoCapture(video_path)
    is_playing = True
    while is_playing:
        ret, frame = cap.read()
        if ret:
            current_frame = frame.copy()
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(cv2image)
            img = ImageTk.PhotoImage(pil_image)
            canvas.create_image(0, 0, anchor=tk.NW, image=img)
            canvas.image = img  # Keep a reference to prevent it from being garbage collected
            window.update()
        else:
            is_playing = False
    cap.release()

def pause_video():
    global is_playing
    is_playing = False

def seek_video():
    global current_frame, cap
    if cap is not None:
        frame_number = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_to_seek = int((seek_scale.get() / 100) * total_frames)
        if frame_to_seek != frame_number:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_to_seek)
            ret, frame = cap.read()
            if ret:
                current_frame = frame.copy()
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(cv2image)
                img = ImageTk.PhotoImage(pil_image)
                canvas.create_image(0, 0, anchor=tk.NW, image=img)
                canvas.image = img  # Keep a reference to prevent it from being garbage collected
                window.update()

# Create the GUI window
window = tk.Tk()
window.title("Video Uploader, Processor, and Player")
window.geometry("1000x600")

# Create the upload window components
upload_frame = tk.Frame(window)
upload_frame.pack(pady=20)

upload_label = tk.Label(upload_frame, text="Upload a video file:")
upload_label.pack()

upload_button = tk.Button(upload_frame, text="Upload", command=open_file)
upload_button.pack(pady=10)

# Create the video canvas
canvas = tk.Canvas(window, width=640, height=480)
canvas.pack(pady=10)

# Create the playback buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

play_button = tk.Button(button_frame, text="Play", command=lambda: play_video(processed_video_path))
play_button.grid(row=0, column=0, padx=5)

pause_button = tk.Button(button_frame, text="Pause", command=pause_video)
pause_button.grid(row=0, column=1, padx=5)

# Create the seek scale
seek_frame = tk.Frame(window)
seek_frame.pack(pady=10)

seek_label = tk.Label(seek_frame, text="Seek:")
seek_label.grid(row=0, column=0)

seek_scale = tk.Scale(seek_frame, from_=0, to=100, orient=tk.HORIZONTAL)
seek_scale.grid(row=0, column=1, padx=5)

seek_button = tk.Button(seek_frame, text="Go", command=seek_video)
seek_button.grid(row=0, column=2, padx=5)

# Create the loading screen
loading_label = tk.Label(window, text="")
loading_label.pack(pady=20)

# Run the GUI
window.mainloop()

