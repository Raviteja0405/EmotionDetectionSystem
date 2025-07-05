# 😊 Emotion Detection Web App

This is a Flask-based web application that detects **human emotions** from images using deep learning. Upload an image with a human face, and the app will predict the emotion expressed.

---

## 📷 Demo

<p align="center">
  <img src="https://private-user-images.githubusercontent.com/125200085/462737037-f37972b5-9b8b-4031-96a0-c1f57d74caac.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE2OTk1MTQsIm5iZiI6MTc1MTY5OTIxNCwicGF0aCI6Ii8xMjUyMDAwODUvNDYyNzM3MDM3LWYzNzk3MmI1LTliOGItNDAzMS05NmEwLWMxZjU3ZDc0Y2FhYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcwNVQwNzA2NTRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00ZTRmOTQyZmFiNDJhOWRhMmI4YjdhMzk5NDFkYWRmZWNlZmViNjYzMzc5Mjg5M2UyMGQ2NmVmZjMwYTE0ODE5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.jQApoZUv5Z6JJ6Dt8DVMYVoJkqJQcz38M2txoiq4lfs" alt="Upload Page Screenshot" style="max-width:100%; height:auto;" />
</p>

<p align="center">
  <img src="https://private-user-images.githubusercontent.com/125200085/462737052-665c3ca5-8fa9-4430-807a-3511a2918738.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE2OTk1MTQsIm5iZiI6MTc1MTY5OTIxNCwicGF0aCI6Ii8xMjUyMDAwODUvNDYyNzM3MDUyLTY2NWMzY2E1LThmYTktNDQzMC04MDdhLTM1MTFhMjkxODczOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcwNVQwNzA2NTRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xNTNhOGYwYTljZjZjYjEwMzM3YjVlOTdiNTM3ZDljNTc1M2IwYjIwNWEyNzBkMDEyOTVjOGUzY2NiZDVlYjAxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.dLyS7bZZRWXLGftoRKUMQcB9lKcKwQ739SmbKaUBH7E" alt="Result Page Screenshot" style="max-width:100%; height:auto;" />
</p>

---

## 🧠 Features

- Upload images via a clean, simple interface  
- Detects faces automatically  
- Classifies emotions into 7 categories:
  - `angry`
  - `disgust`
  - `fear`
  - `happy`
  - `neutral`
  - `sad`
  - `surprise`
- Shows the detected emotion label along with annotated image  

---

## 🛠️ Technologies Used

- Python 3.8  
- Flask  
- OpenCV  
- TensorFlow / Keras  
- HTML & CSS  

---

## 📁 Project Structure

```

emotion-detection-app/
├── app/
│   ├── static/
│   │   ├── css/
│   │   └── uploads/           # Uploaded and result images
│   └── templates/
│       └── index.html         # Main webpage
├── trained\_models/
│   └── emotion\_model.h5       # Pretrained emotion detection model
├── train.py                   # Model training script (optional)
├── main.py                    # Flask application entry point
├── requirements.txt           # Python dependencies
└── README.md

````

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/emotion-detection-app.git
cd emotion-detection-app
````

### 2. (Optional but recommended) Create and activate a virtual environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app

```bash
python main.py
```

Open your browser at `http://127.0.0.1:5000/`

---

## 🧪 Dataset Format (if training)

Dataset should be organized as:

```
dataset/
├── train/
│   ├── angry/
│   ├── happy/
│   └── ...
└── test/
    ├── angry/
    ├── happy/
    └── ...
```

You can use the [FER2013 dataset on Kaggle](https://www.kaggle.com/datasets/msambare/fer2013) or similar.

---

## 📸 How to Use

1. Upload an image with a clear human face.
2. The app detects the face and predicts the emotion.
3. The result page displays the detected emotion and annotated image.

---

## 📦 Recommended .gitignore

```
__pycache__/
*.py[cod]
venv/
.env
*.log
.DS_Store
*.swp
*.h5
app/static/uploads/
static/uploads/
trained_models/
```

---

## 🧑‍💻 Author

Made with ❤️ by Ravi Teja
[GitHub](https://github.com/Raviteja0405)

---

## 📝 License

This project is licensed under the MIT License.