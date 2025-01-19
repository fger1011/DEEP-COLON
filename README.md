# DEEP-COLON

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)

## Description
DEEP-COLON is a standalone software program that detect colon polyps from a colonoscopy video that identifies and categorize the polyp either a polyp or a diverticula. This software project benefits a client from MD Sinai Laguna Hospital that contributed for the project. This program uses YOLOv4 tiny for detecting colorectal abnormalities which improves FPS for every uploaded video. This project still needs improvement and it far from being perfect. 

## YOLOv4 vs YOLOv4-tiny

YOLOv4 is an object detection algorithm that is an evolution of the YOLOv3 model. The YOLOv4 method was created by Alexey Bochkovskiy, Chien-Yao Wang, and Hong-Yuan Mark Liao. It is twice as fast as EfficientDet with comparable performance. In addition, AP (Average Precision) and FPS (Frames Per Second) in YOLOv4 have increased by 10% and 12% respectively compared to YOLOv3.

YOLOv4-tiny is the compressed version of YOLOv4. It is proposed based on YOLOv4 to make the network structure simpler and reduce parameters so that it becomes feasible for developing on mobile and embedded devices.

We can use YOLOv4-tiny for faster training and faster detection. It has only two YOLO heads as opposed to three in YOLOv4 and it has been trained from 29 pre-trained convolutional layers as opposed to YOLOv4 which has been trained from 137 pre-trained convolutional layers.

The FPS (Frames Per Second) in YOLOv4-tiny is approximately eight times that of YOLOv4. However, the accuracy for YOLOv4-tiny is 2/3rds that of YOLOv4 when tested on the MS COCO dataset.

The YOLOv4-tiny model achieves 22.0% AP (42.0% AP50) at a speed of 443 FPS on RTX 2080Ti, while by using TensorRT, batch size = 4 and FP16-precision the YOLOv4-tiny achieves 1774 FPS.

For real-time object detection, YOLOv4-tiny is the better option when compared with YOLOv4 as faster inference time is more important than precision or accuracy when working with a real-time object detection environment.

## User Interface

### Login Window
![Image](https://github.com/user-attachments/assets/f5785a65-97ae-4cc6-9d2d-b89dc2f4a44d)

### Home Window
![Image](https://github.com/user-attachments/assets/f4dac78a-ca1d-4750-9f0c-eabfcf09c71d)

### Uploaded Video
![Image](https://github.com/user-attachments/assets/dfdd6bf8-d08e-4cb7-95ff-3991c06aa467)

### Automated Message after Upload 
![Image](https://github.com/user-attachments/assets/cdd5d025-cfa1-4180-81a3-00879e4c0bef)


## Sample Output

![Image](https://github.com/user-attachments/assets/93ae3118-4df3-43ec-97ab-aa904a8a3746)

## License

MIT License

Copyright (c) 2024 Franco Gian Ramos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files DEEP-COLON, to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

