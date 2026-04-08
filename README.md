# Emotion-Detection-for-visual-content-using-OpenCV-and-Mediapipe-Landmarks-classification
## Overview
This project presents an AI-powered emotion detection system designed to assist visually impaired individuals in understanding human emotions. The system analyzes facial expressions from images and video streams in real time and provides both visual and auditory feedback, enhancing communication and independence.

## Motivation
Visually impaired individuals face significant challenges in recognizing emotions and engaging in social interactions. This project aims to bridge that gap by providing an intelligent system that interprets facial expressions and conveys emotional information through speech, reducing reliance on others.

## Methodology

### 1. Data Processing
- Facial landmarks are extracted using **MediaPipe Face Mesh (Holistic model)**.  
- Key facial features such as eyes, lips, and eyebrows are analyzed.  
- Landmark coordinates are processed using **NumPy**.  
- Dataset is organized into emotion categories (e.g., happy, sad, surprised).  

### 2. Model Training
- A **Random Forest Classifier** is used for emotion classification.  
- Data is split into training and testing sets using **scikit-learn**.  
- Model performance is evaluated using:
  - Accuracy Score  
  - Confusion Matrix  
- The trained model is saved using **pickle**.  

### 3. Real-Time Emotion Detection
- Video input is processed using **OpenCV**.  
- Facial landmarks are extracted frame-by-frame.  
- The trained model predicts emotions in real time.  
- Results are displayed on screen and converted to speech using **pyttsx3**.  

## Technologies Used
- Python  
- OpenCV  
- MediaPipe  
- Scikit-learn  
- NumPy  
- Pickle  
- Pyttsx3  

## Features
- Real-time emotion detection from video input  
- Facial landmark analysis using computer vision  
- Audio feedback describing detected emotions  
- Enhances accessibility for visually impaired users  

## Dataset
The project includes a `DATA/` folder containing sample images organized into different emotion categories (e.g., happy, sad, surprised).

Note: The dataset provided is relatively small and intended for demonstration purposes only. Users are encouraged to expand the dataset with their own images to improve model accuracy and performance.

## Results
- Achieved an accuracy of **75.76%** on the test dataset  
- Successfully detected emotions such as *happy, sad, and surprised*  
- Output includes:
  - Facial mesh visualization  
  - Emotion label displayed on screen  
  - Spoken emotion feedback  

## Testing
To validate the system, we used sample video files:
- `sadMan.mp4`
- `peopleSmile.mp4`

These videos were used to test the model and ensure correct real-time emotion detection.

## How to Run the Project

### 1. Prepare the Dataset
```bash
python prepare_data.py
```
This script extracts facial landmarks from images and generates a file called `data.txt`.

---

### 2. Train the Model
```bash
python train_model.py
```
This will:
- Train the model  
- Evaluate its performance  
- Save it as `model`  

---

### 3. Test the Model
```bash
python Test_Model.py
```
This will:
- Open a test video  
- Detect emotions in real time  
- Display results on screen  
- Provide audio feedback  

Press `q` to exit.

---

## Conclusion
This project demonstrates the potential of AI and computer vision in improving accessibility for visually impaired individuals. By combining emotion recognition with real-time audio feedback, the system enhances communication and independence.
