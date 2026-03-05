# 🍾 Bottle Detection using OpenCV + YOLOv8

Welcome! 👋  
This project detects **bottles in real-time** from your webcam using:

- 🧠 `Ultralytics YOLOv8`
- 📷 `OpenCV`
- 🐍 `Python`

---

## ✨ What this project does

- Opens your webcam
- Runs YOLOv8 inference on each frame
- Detects only the **bottle class**
- Draws a green box and label: **Bottle Detected**

---

## 📁 Project Structure

```bash
.
├── vision1.py
├── yolov8n.pt
└── README.md
```

---

## 🛠️ Setup From Scratch (Beginner Friendly)

### 1) Create project folder

```bash
mkdir bottle-detection-using-opencv
cd bottle-detection-using-opencv
```

### 2) Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Install required libraries

```bash
pip install --upgrade pip
pip install ultralytics opencv-python
```

### 4) Create the Python file

Create a file named `vision1.py` and paste your bottle detection code inside it.

### 5) Add model weights

Option A ✅ (recommended): keep `yolov8n.pt` in the same folder as `vision1.py`.  
Option B ✅: if `yolov8n.pt` is missing, Ultralytics may auto-download it the first time (internet required).

---

## ▶️ Run the project

```bash
source venv/bin/activate
python3 vision1.py
```

Press **`q`** to quit the webcam window.

---

## 📦 Requirements

- Python 3.8+
- Webcam access
- Linux/macOS/Windows (commands above are Linux/macOS style)

---

## 🧪 Common Issues & Quick Fixes

### Camera not opening? 📷

- Close other apps using the camera
- Try running again
- On Linux, check camera devices:

```bash
ls /dev/video*
```

### `ModuleNotFoundError`? 🐍

Install missing packages inside your virtual environment:

```bash
pip install ultralytics opencv-python
```

---

## 🚀 Future Improvements

- Save detection video output
- Count bottles per frame
- Add confidence score display
- Build a simple GUI/web dashboard

---

## 🙌 Author

Made with passion by **DropPlan-at13** 💙

If you like this project, give it a ⭐ on GitHub!