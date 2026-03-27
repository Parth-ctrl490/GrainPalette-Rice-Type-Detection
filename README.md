# 🌾 GrainPalette - Rice Type Detection

> A Deep Learning Odyssey In Rice Type Classification Through Transfer Learning

---

## 📌 About The Project

The Rice Type Identification AI model provides a solution for farmers and agriculture enthusiasts to identify various types of rice grains quickly and accurately. By uploading an image of a rice grain and clicking the submit button, users receive predictions for the probable type of rice.

Built using **Convolutional Neural Networks (CNN)** and **Transfer Learning with MobileNetV2**, this model classifies **5 different types of rice** with over **97% accuracy**.

---

## 🎯 Use Case Scenarios

### 🌱 Farmers Crop Planning
Farmers can upload images of rice grains to determine the specific types they possess and adjust irrigation, fertilization, and pest management accordingly.

### 🔬 Research and Agricultural Extension Services
Agriculture scientists can capture images of rice grains during field visits and obtain rapid classifications to facilitate data collection for research studies.

### 🏡 Home Gardening and Education
Home growers can explore the diversity of rice types and understand their unique characteristics.

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

## 🏗️ Technical Architecture

| Component | Details |
|-----------|---------|
| Base Model | MobileNetV2 pretrained on ImageNet |
| Input Shape | 224 x 224 x 3 |
| Output Classes | 5 Rice Types |
| Total Parameters | 2,264,389 |
| Trainable Parameters | 6,405 |
| Optimizer | Adam |
| Loss Function | SparseCategoricalCrossentropy |

---

## 🗂️ Project Structure
```
GrainPalette-Rice-Type-Detection/
├── static/
│   ├── uploads/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── details.html
│   └── results.html
├── app.py
├── rice.h5
├── rice-classification-1.ipynb
└── GrainPalette_Report.docx
```

---

## 🚀 How To Run

1. Install dependencies:
```
pip install flask tensorflow opencv-python numpy scikit-learn
```

2. Run the app:
```
python app.py
```

3. Open in browser:
```
http://127.0.0.1:5000
```

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)

---

## 📊 Dataset

- Source: [Kaggle - Rice Image Dataset](https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset)
- Total Images: 3,000 (600 per class)

---

## 👨‍💻 Author

**Parth Shukla** — [@Parth-ctrl490](https://github.com/Parth-ctrl490)

---

⭐ Star this repo if you found it helpful!
