# 🌾 GrainPalette - Rice Type Detection

> **A Deep Learning Odyssey In Rice Type Classification Through Transfer Learning**

"C:\Users\HP\Pictures\Screenshots\Screenshot 2026-03-27 153900.png"

---

## 📌 About The Project

The **Rice Type Identification AI model** provides a solution for farmers and agriculture enthusiasts to identify various types of rice grains quickly and accurately. By uploading an image of a rice grain and clicking the submit button, users receive predictions for the probable type of rice, enabling informed decisions on cultivation practices such as water and fertilizer requirements.

Built using **Convolutional Neural Networks (CNN)** and employing **Transfer Learning with MobileNetV2**, this model offers reliable classification of up to **five different types of rice**, catering to the needs of farmers, agriculture scientists, home growers, and gardeners.

---

## 🎯 Use Case Scenarios

### 🌱 Farmers' Crop Planning
Farmers can use the model to plan crop cultivation strategies. Before planting, they can upload images of rice grains to determine the specific types they possess and adjust irrigation, fertilization, and pest management accordingly.

### 🔬 Research and Agricultural Extension Services
Agriculture scientists and extension workers can capture images of rice grains during field visits and obtain rapid classifications to facilitate data collection for research studies and variety testing.

### 🏡 Home Gardening and Education
Home growers can explore the diversity of rice types, understand their unique characteristics, and promote sustainable practices in home gardening.

---

## 🖼️ Project Screenshots

### 🏠 Home Page
![Home Page](static/uploads/Screenshot%202026-03-27%20143309.png)

### 🔍 Prediction Result - Basmati Rice (99.95% Confidence)
![Result Page](static/uploads/Screenshot%202026-03-27%20143252.png)

### 📊 Training & Evaluation Accuracy
![Accuracy Graph](static/uploads/Screenshot%202026-03-25%20095454.png)

### 📉 Training & Evaluation Loss
![Loss Graph](static/uploads/Screenshot%202026-03-27%20143259.png)

### 🌾 Rice Categories Visualization
![Rice Categories](static/uploads/Screenshot%202026-03-27%20143303.png)

---

## 🏗️ Technical Architecture

```
Images → Preprocessing → MobileNetV2 (frozen) → GlobalAveragePooling2D → Dense(5) → Prediction
```

| Component | Details |
|-----------|---------|
| Base Model | MobileNetV2 (pretrained on ImageNet) |
| Input Shape | 224 x 224 x 3 |
| Output Classes | 5 Rice Types |
| Total Parameters | 2,264,389 |
| Trainable Parameters | 6,405 |
| Optimizer | Adam |
| Loss Function | SparseCategoricalCrossentropy |

---

## 🌾 Rice Classes

| Class | Label | Description |
|-------|-------|-------------|
| Arborio | 0 | Short-grain Italian rice used for risotto |
| Basmati | 1 | Long-grain aromatic rice from the Himalayas |
| Ipsala | 2 | Medium-grain Turkish variety |
| Jasmine | 3 | Fragrant long-grain rice from Southeast Asia |
| Karacadag | 4 | Traditional Turkish short-grain rice |

---

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| Training Accuracy | ~99.24% |
| Validation Accuracy | ~96.81% |
| Test Accuracy | ~97.51% |
| Test Loss | ~0.0943 |

---

## 🗂️ Project Structure

```
GrainPalette-Rice-Type-Detection/
├── 📁 static/
│   ├── 📁 uploads/          ← Uploaded images stored here
│   └── 🎨 style.css         ← External CSS stylesheet
├── 📁 templates/
│   ├── 🌐 index.html        ← Home page
│   ├── 🌐 details.html      ← Image upload page
│   └── 🌐 results.html      ← Prediction results page
├── 🐍 app.py                ← Flask application
├── 📓 rice-classification-1.ipynb  ← Training notebook
├── 🤖 rice.h5               ← Saved trained model
├── 📄 GrainPalette_Report.docx     ← Project report
└── 📄 Rice_Type_Classification.docx
```

---

## 🚀 How To Run

**1. Install dependencies:**
```bash
pip install flask tensorflow opencv-python numpy scikit-learn
```

**2. Run the Flask app:**
```bash
python app.py
```

**3. Open in browser:**
```
http://127.0.0.1:5000
```

**4. Upload a rice grain image and get instant prediction!** 🌾

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

---

## 👨‍💻 Author

**Parth Shukla**
- GitHub: [@Parth-ctrl490](https://github.com/Parth-ctrl490)

---

## 📊 Dataset

- **Source:** [Kaggle - Rice Image Dataset](https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset)
- **Author:** Murat Koklu
- **Total Images:** 15,000 (3,000 used - 600 per class)

---

⭐ **If you found this project helpful, please give it a star!** ⭐
