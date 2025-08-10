# 🎨 Virtual Paint

**Virtual Paint** is an interactive computer vision project that allows you to draw in the air using hand gestures or a colored object.  
It uses **OpenCV** to detect and track a specific color in real-time and translates its movement into brush strokes on a digital canvas.

---

## 📌 Project Info

**Author:** [AnirudhNarang15](https://github.com/AnirudhNarang15)  

---

## 📂 Repository Contents
1. code.py # Main script for Virtual Paint functionality
2. colorpick.py # Utility script to pick and calibrate pen color (HSV range)
3. modified.py # Alternate implementation with changes/improvements
4. pens.npy # NumPy file storing predefined pen colors

## 🛠️ Requirements

Make sure you have **Python 3.x** installed along with the following libraries:

```bash
pip install opencv-python numpy
```

## 🎯 Features

Real-time color tracking using OpenCV.

HSV slider-based color calibration.

Ability to draw in air using a physical colored object.

Multiple pen colors stored in pens.npy.

Canvas clearing functionality.

Alternate implementation with improved logic in modified.py.

## 📸 How It Works

Color Detection: The system uses HSV color space for robust color tracking.

Masking & Contour Detection: The object of the specified color is detected using masks and contours.

Drawing on Canvas: The detected position is mapped to a canvas for real-time drawing.

Customization: Colors and ranges are adjustable for better accuracy.
