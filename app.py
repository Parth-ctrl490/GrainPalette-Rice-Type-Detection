from flask import Flask, request, render_template, redirect, url_for
import numpy as np
import cv2
import os
from tensorflow import keras

app = Flask(__name__)

model = keras.models.load_model('rice.h5')

labels = {
    0: 'Arborio',
    1: 'Basmati',
    2: 'Ipsala',
    3: 'Jasmine',
    4: 'Karacadag'
}

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return redirect(url_for('details'))

    file = request.files['image']
    if file.filename == '':
        return redirect(url_for('details'))
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    img = cv2.imread(filepath)
    img = cv2.resize(img, (224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    predicted_label = labels[np.argmax(prediction)]
    confidence = round(float(np.max(prediction)) * 100, 2)
    return render_template('results.html',
                           prediction=predicted_label,
                           confidence=confidence,
                           image_path=filepath)

if __name__ == '__main__':
    app.run(debug=True)