# Face Recognition with Occlusion Handling Using Deep Learning

## 📌 Project Overview
This project is an AI-powered Face Detection and Recognition system capable of recognizing faces even when partially covered with masks or occlusions. The system improves traditional face recognition methods by integrating modern deep learning models such as DeepFace (FaceNet), RetinaFace/Mediapipe, and the Segment Anything Model (SAM).

The project uses Python, OpenCV, DeepFace, and SQLite for real-time face detection and recognition.

---

# 🚀 Features

- Real-time face detection using webcam
- Face recognition using FaceNet embeddings
- Recognition of masked and unmasked faces
- Occlusion handling support
- Improved detection accuracy using RetinaFace/Mediapipe
- Unknown face rejection system
- SQLite database integration
- Dataset generation and training pipeline
- Easy-to-use interface

---

# 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Image processing and webcam handling |
| DeepFace | Face recognition and embeddings |
| FaceNet | Feature extraction model |
| RetinaFace / Mediapipe | Advanced face detection |
| SAM (Segment Anything Model) | Occlusion-aware segmentation |
| SQLite | Database storage |
| NumPy | Numerical computations |
| TensorFlow / PyTorch | Deep learning backend |

---

# 📂 Project Structure

```bash
FaceRecognitionProject/
│
├── dataset/                 # Stored face images
├── trainer/                 # Saved embeddings and trained data
├── database/                # SQLite database
├── models/                  # Deep learning models
├── detect.py                # Real-time face detection
├── trainer.py               # Embedding extraction and training
├── dataset_generator.py     # Dataset collection
├── database.py              # Database operations
├── requirements.txt         # Required libraries
└── README.md                # Project documentation
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/face-recognition-occlusion.git
cd face-recognition-occlusion
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Required Libraries

```txt
opencv-python
numpy
deepface
tensorflow
mediapipe
retina-face
sqlite3
Pillow
```

---

# 📸 Dataset Collection

Run the dataset generator:

```bash
python dataset_generator.py
```

Instructions:
- Enter user ID and name
- Capture multiple face images
- Capture both masked and unmasked images
- Images are stored in the dataset folder

---

# 🧠 Training the Model

Run:

```bash
python trainer.py
```

This step:
- Extracts embeddings using FaceNet
- Stores embeddings
- Trains recognition pipeline
- Saves trained data

---

# 🎥 Real-Time Detection

Run:

```bash
python detect.py
```

The system will:
- Detect faces in real time
- Compare embeddings with trained data
- Display user name if matched
- Display “Unknown” for unregistered faces

---

# 🧩 Occlusion Handling

This project improves masked face recognition using:

- DeepFace FaceNet embeddings
- SAM segmentation
- Additional masked-face dataset samples
- RetinaFace/Mediapipe detection

The system focuses on visible facial regions such as:
- Eyes
- Forehead
- Face structure

---

# 🔍 How Recognition Works

1. Webcam captures frame
2. Face detector identifies faces
3. Face is cropped and preprocessed
4. FaceNet extracts embeddings
5. Embeddings are compared with stored vectors
6. Best similarity match is selected
7. Identity displayed on screen

---

# 🗄 Database Structure

The SQLite database stores:

| Field | Description |
|---|---|
| ID | User ID |
| Name | User Name |
| Embedding Path | Stored embedding location |

---

# 📈 Future Improvements

- Multi-face tracking
- Attendance system integration
- Cloud database support
- Mobile app integration
- Higher accuracy models
- Liveness detection
- Anti-spoofing techniques

---

# 🐞 Common Issues and Fixes

## Problem: Faces always detected as “Unknown”

### Solution:
- Retrain embeddings using trainer.py
- Ensure same FaceNet model is used
- Check embedding threshold values
- Add more dataset images

---

## Problem: Unregistered faces recognized incorrectly

### Solution:
- Increase similarity threshold
- Improve dataset quality
- Use more training samples
- Add masked and unmasked data

---

# 📊 Applications

- Smart attendance systems
- Secure authentication
- Surveillance systems
- AI-based security systems
- Smart classrooms
- Office access control

---

# 🎯 Advantages

- High recognition accuracy
- Real-time performance
- Supports masked faces
- Lightweight implementation
- Easy integration

---

# ⚠️ Limitations

- Accuracy may reduce in poor lighting
- Requires good dataset quality
- High-resolution camera recommended

---

# 👨‍💻 Author

Jagan V

B.Tech Computer science
College of Engineering and Management Punnapra, Kerala
Department of Computer Science and Engineering

---

# 📜 License

This project is developed for educational and research purposes.

---

# ⭐ Acknowledgment

Special thanks to:
- OpenCV Community
- DeepFace
- FaceNet Researchers
- Meta AI SAM Model
- Python Open Source Community

