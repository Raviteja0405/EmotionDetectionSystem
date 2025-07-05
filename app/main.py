# Import necessary libraries
import os
from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__, static_url_path='/static')

# Load the trained emotion recognition model
model_path = 'trained_models/emotion_model.h5'
emotion_model = load_model(model_path)

# Load the OpenCV face detection cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Define the emotion labels
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# Folder to store uploaded images
UPLOAD_FOLDER = 'app/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def predict_emotion(img_path):
    # Read the uploaded image using OpenCV
    img = cv2.imread(img_path)

    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # For each detected face, predict emotion and draw rectangle
    for (x, y, w, h) in faces:
        # Extract the face region
        face_roi = img[y:y+h, x:x+w]

        # Ensure that face_roi is a three-channel image
        if face_roi.shape[-1] == 1:
            # Convert grayscale image to three channels
            face_roi = cv2.cvtColor(face_roi, cv2.COLOR_GRAY2BGR)

        # Preprocess the face for emotion prediction
        face_roi = cv2.resize(face_roi, (48, 48))
        face_roi = np.expand_dims(face_roi, axis=0)  # Add batch size dimension
        face_roi = face_roi / 255.0

        # Make emotion prediction using the loaded model
        predictions = emotion_model.predict(face_roi)
        predicted_label = emotion_labels[np.argmax(predictions)]

        # Draw rectangle around the face
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display emotion text below the rectangle
        # cv2.putText(img, f'{predicted_label}', (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    return img, predicted_label


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded image file
    image_file = request.files['image']

    # Save the image temporarily in the uploads folder
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_image.jpg')
    image_file.save(image_path)

    # Predict emotion and draw rectangles on faces
    img_with_faces, predicted_label = predict_emotion(image_path)

    # Save the image with rectangles temporarily
    result_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result_image.jpg')
    cv2.imwrite(result_image_path, img_with_faces)

    if os.path.exists(result_image_path):
        print("Image file exists.")
        print(result_image_path)
    else:
        print("Image file does not exist.")

    if isinstance(img_with_faces, np.ndarray):
        cv2.imwrite(result_image_path, img_with_faces)

        # Return the result image path and predicted emotion
        return render_template('index.html', result_image_path=os.path.basename(result_image_path), emotion=predicted_label)

    # Return the result image path
    return render_template('index.html', result_image_path=os.path.basename(result_image_path))


if __name__ == '__main__':
    app.run(debug=True)
