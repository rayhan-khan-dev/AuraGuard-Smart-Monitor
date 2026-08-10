# 🛡️ AuraGuard — The Smart Workspace & Hydration Monitor

> **An ambient, privacy-first computer vision assistant that monitors workspace focus and hydration in real-time using YOLO and OpenCV.**

---

## 📌 Project Overview

In remote work and digital learning environments, **smartphone distractions** and **dehydration** are two silent productivity killers. Traditional apps rely on manual logs or rigid timers that do not reflect actual human behavior.

**AuraGuard** solves this by leveraging real-time computer vision. Utilizing a standard webcam and pre-trained YOLO object detection, AuraGuard monitors your desk environment, tracks phone usage duration, estimates hydration intervals using temporal state logic, and displays a dynamic Heads-Up Display (HUD) directly on your video stream.

---

## ✨ Key Features

- **📱 Phone Distraction Alert:** Tracks active smartphone usage and triggers visual HUD warnings when distraction exceeds threshold limits.
- **💧 Smart Hydration Tracking:** Utilizes temporal state logic to track time elapsed since the last drink was detected.
- **⚡ Lightweight & Privacy-First:** Runs 100% locally on device using lightweight model architecture (`YOLOv8n` / `YOLOv11n`).
- **🎯 Dynamic OpenCV HUD:** Direct frame overlays displaying system states, bounding boxes, timers, and alert banners.
- **⚙️ Configurable Thresholds:** Flexible time limits for fast testing or production workspace monitoring.

---

## 🧠 System Architecture & Temporal Logic

AuraGuard continuously evaluates the webcam feed and handles state transitions through class filtering and temporal condition tracking:
```bash
┌──────────────────────────────┐
              │      Webcam Video Feed       │
              └──────────────┬───────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │    YOLO Detection Stream     │
              └──────────────┬───────────────┘
                             │
             ┌───────────────┴───────────────┐
             │  Filter COCO Classes          │
             │  (Person, Phone, Cup, Bottle) │
             └───────────────┬───────────────┘
                             │
     ┌───────────────────────┴───────────────────────┐
     ▼                                               ▼
┌──────────────────────────────┐                ┌──────────────────────────────┐
│       Phone Tracking         │                │      Hydration Tracking      │
├──────────────────────────────┤                ├──────────────────────────────┤
│ Detect: cell phone           │                │ Detect: cup / bottle         │
│ Rule: Trigger alert if usage │                │ Rule: Reset timer when seen; │
│ duration > threshold.        │                │ alert if missing > threshold.│
└──────────────┬───────────────┘                └──────────────┬───────────────┘
│                                               │
└───────────────────────┬───────────────────────┘
│
▼
┌─────────────────────────────┐
│   Dynamic OpenCV HUD Layer  │
└─────────────────────────────┘
```
---

## 🛠️ Technology Stack

- **Language:** Python 3.9+
- **Computer Vision:** OpenCV (`cv2`)
- **Object Detection:** Ultralytics YOLO (`YOLOv8` / `YOLOv11` / `YOLOv26`)
- **Time Logic:** Python `time` module

---

## 📊 Class ID Mapping (COCO Dataset)

| Target Object | Class Name | Class ID |
| :--- | :--- | :--- |
| **User** | `person` | `0` |
| **Distraction** | `cell phone` | `67` |
| **Hydration Source** | `bottle` | `39` |
| **Hydration Source** | `cup` | `41` |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/rayhan-khan-dev/AuraGuard-Smart-Monitor](https://github.com/rayhan-khan-dev/AuraGuard-Smart-Monitor).
cd AuraGuard
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
Bash
pip install ultralytics opencv-python numpy
```

### 4. Run the Application
```bash
Bash
python main.py
Note: Press q to safely exit the application stream.
```

## ⚙️ Configuration Options
```bash
You can adjust detection thresholds directly in the script for demonstration or production use:

Python
# System Thresholds (in seconds)
PHONE_ALERT_THRESHOLD = 5     # Alert after 5 seconds of phone usage
HYDRATION_ALERT_THRESHOLD = 30 # Alert after 30 seconds without drinking (Demo mode)
CONFIDENCE_THRESHOLD = 0.40   # Minimum detection confidence
```

## 📂 Repository Structure
```bash
├── main.py               # Main application loop, YOLO inference & HUD rendering
├── requirements.txt      # Project dependencies
├── assets/               # Demo videos, screenshots, and diagrams
└── README.md             # Project documentation
```
## 👨‍💻 Author

GitHub: https://github.com/rayhan-khan-dev

LinkedIn: www.linkedin.com/in/rayhan-khan-dev
