# 🛰️ Satellite Image Anomaly Detector

My first AI/ML project for detecting unusual regions in satellite images using Python and OpenCV.

## 📌 Project Overview

This project analyzes a satellite image and identifies regions that are significantly different from their surrounding areas.

The detected regions are highlighted with red bounding boxes, and the program calculates the percentage of the image considered unusual by the detection method.

> Note: This is a beginner prototype using image-processing techniques. The detected regions are not automatically confirmed real-world satellite anomalies.

## 🚀 Features

- Loads satellite images
- Converts images to grayscale
- Detects unusual local regions
- Removes small noisy regions
- Finds separate anomaly regions
- Draws bounding boxes around detected regions
- Calculates anomaly percentage
- Saves the processed result image

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy
- VS Code

## ⚙️ How It Works

Satellite Image  
↓  
Image Loading  
↓  
Grayscale Conversion  
↓  
Local Difference Detection  
↓  
Noise Removal  
↓  
Anomaly Region Detection  
↓  
Bounding Boxes  
↓  
Anomaly Percentage  
↓  
Result Image

## 📊 Current Test Result

For the current test image:

- Anomaly regions detected: **7**
- Anomaly percentage: **0.02%**

## ▶️ How to Run

```bash
python src/main.py