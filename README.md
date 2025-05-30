# Face Recognition Attendance System

A complete **Face Recognition Attendance System** built using Python, OpenCV, and Tkinter. This system automates attendance tracking in real-time by detecting and recognizing student faces. It provides an easy-to-use GUI for managing student data, capturing facial images, training a model, and marking attendance.

## Features

- Student management (Add/Update/Delete student info)
- Real-time face detection & recognition using webcam
- LBPH-based face training model (`classifier.xml`)
- SQLite/MySQL database integration for student records
- CSV import/export for attendance reports
- GUI-based using Tkinter with multi-window navigation
- Auto-attendance with date, time, and department
- Data stored and retrieved securely

## Tech Stack

- **Frontend**: Tkinter (Python GUI)
- **Backend**: Python
- **Face Recognition**: OpenCV (LBPH + Haar Cascades)
- **Database**: SQLite or MySQL (configurable)
- **Others**: PIL, Numpy, OS, DateTime, CSV

## How It Works

### 1. Student Registration
- User enters student info (name, roll number, department, etc.).
- System captures face images via webcam.
- Images are saved in `data/` folder with format `User.<id>.<image_no>.jpg`.

### 2. Model Training
- `train.py` scans the `data/` folder.
- Converts images to grayscale and extracts labels (IDs).
- Trains the **LBPH face recognizer** and saves it as `classifier.xml`.

### 3. Real-Time Face Recognition
- Webcam feed is opened.
- Faces are detected using the **Haar Cascade classifier**.
- Recognized faces are matched using the **trained LBPH model**.
- On successful match, student data is fetched from the database.

### 4. Attendance Marking
- If a student is recognized, their attendance is marked with:
  - ID, Name, Roll No, Department, Date, Time, and Status.
- Attendance records are displayed in a table and can be exported as a `.csv`.



