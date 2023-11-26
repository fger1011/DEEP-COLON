import subprocess
import cv2
import os


folder_path = "screenshots/Untitled video - Made with Clipchamp"


def process_video(video_path):
    global processed_video_path, total_frames
    # Define the output video path
    output_dir = "./outputs"
    os.makedirs(output_dir, exist_ok=True)
    processed_video_path = os.path.join(output_dir, "processed_video.mp4")

    # Run the object_tracker.py script as a subprocess, passing the video path and output video path as arguments

    # command = ['python', 'object_tracker.py', '--video', video_path, '--output', processed_video_path, '--model', 'yolov4']
    # subprocess.run(command)

    # os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # Replace '0' with the GPU device index you want to use
    # Path to the save_model.py script
    save_model_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\save_model.py"

    # Path to the weights file
    weights_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\data\yolov4-tiny-obj_last (1).weights"

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

    command = ['python', 'object_tracker.py', '--video', video_path, '--output', processed_video_path, '--weights',
               './checkpoints/yolov4-tiny-416', '--model', 'yolov4']

    subprocess.run(command)

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()


    # Play the processed video




