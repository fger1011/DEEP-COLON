import tkinter as tk
from tkinter import filedialog
import cv2


def upload_video():
    # Open file dialog to select the video file
    file_path = filedialog.askopenfilename(filetypes=[("MP4 Videos", "*.mp4")])

    # Check if a file was selected
    if file_path:
        # Process the video
        process_video(file_path)


def process_video(file_path):
    # Open the video file
    video = cv2.VideoCapture(file_path)

    # Read the frames
    while True:
        ret, frame = video.read()

        # Check if frame was read successfully
        if ret:
            # Process the frame (add your custom processing code here)
            # For example, you can display the frame in a separate window
            cv2.imshow("Video", frame)

            # Exit if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release the video object and destroy the windows
    video.release()
    cv2.destroyAllWindows()


# Create the GUI window
window = tk.Tk()
window.title("MP4 Video Uploader")

# Create the "Upload" button
upload_button = tk.Button(window, text="Upload MP4 Video", command=upload_video)
upload_button.pack(pady=20)

# Run the GUI window
window.mainloop()
