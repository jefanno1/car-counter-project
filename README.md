# 🚗 Real-Time Vehicle Counter using YOLOv8 & ByteTrack

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![YOLO](https://img.shields.io/badge/YOLO-v8-yellow.svg)

> A high-performance Computer Vision system that detects, tracks, and counts vehicles in real-time using YOLOv8 and ByteTrack.

---

## 🎬 Demo

![Car Counter Demo](./detection/hasil_car_counter.gif)

---

## 🚀 Key Features

* **Real-Time Vehicle Detection**  
  Utilizes YOLOv8n for fast and accurate detection of vehicles in video streams.

* **Robust Multi-Object Tracking**  
  Implements ByteTrack to maintain consistent IDs for each vehicle across frames.

* **Region-Based Counting System**  
  Counts vehicles when they cross a predefined virtual line (ROI-based counting).

* **Efficient Video Processing**  
  Outputs annotated video with bounding boxes, object IDs, and live counting.

---

## 🛠️ Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/jefanno1/car-counter-project.git
cd car-counter-project
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Model And Source Videos

Download model and video here -> https://drive.google.com/drive/folders/1-h1Pc9BjpofJWDAnZ-x_s85MxzyhlWnj?usp=drive_link

* Create 'model' folder and 'source' folder
* put yolov8n.pt inside of 'model' and cars.mp4 inside of 'source'

---

### 4. Run the System

```bash
python Car_Counter_main.py
```

Press q to exit the video window.

---

## 🧠 Under the Hood (Technical Highlights)

### Real-Time Detection + Tracking Pipeline

This project combines:

* YOLOv8 → Performs high-speed object detection.
* ByteTrack → Manages object association, ensuring that a vehicle identified in Frame 10 is the same vehicle in Frame 11, preventing ID switches.

Each detected vehicle is assigned a unique ID, allowing the system to track movement across frames and avoid double counting.

---

### Region of Interest (ROI) Filtering

To improve accuracy and reduce false detections:

* A binary mask.png is applied to isolate the road area.
* This ignores background activity and focus computations only on the relevant traffic flow.

This ensures system stability even under noisy detection conditions.

---

### Line-Crossing Counting Mechanism

Vehicle counting is based on a virtual line:

```python
if limits[0] < cx < limits[2] and limits[1] - 20 < cy < limits[3] + 20:
```

This ensures that only vehicles crossing the defined coordinate plane increment the counter, preventing double-counting.

---

## 📌 Notes

* GPU Recommended: For smooth real-time performance, running this on a machine with a CUDA-enabled GPU is highly recommended.
* Masking: If detection is inaccurate, recreate mask.png to perfectly align with the specific road perspective of your input video.
* Tuning: You can adjust the limits array in Car_Counter_main.py to match the specific camera angle and road width of your footage.

---

## 📁Project Structure

car-counter-project/
│
├── detection/
│   └── hasil_car_counter.mp4
│
├── source/
│   └── cars.mp4
│
├── model/
│   └── yolov8n.pt
├── mask.png
├── Car_Counter_main.py
└── requirements.txt

---

## 🙌 Acknowledgments

* YOLOv8 for object detection framework
* OpenCV for real-time image processing
* Python ecosystem for rapid development and optimization

---

## 📄 License

[MIT License](LICENSE)

---
