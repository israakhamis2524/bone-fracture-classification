# 🦴 Bone Fracture Classification using Deep Learning

This project aims to **automatically classify bone fractures** from X-ray images using **MobileNetV2** and **Convolutional Neural Networks (CNNs)**. The system is designed to distinguish between two types of fractures:

- **Comminuted Bone Fracture**
- **Simple Bone Fracture**

---

## 🧠 Project Motivation

Bone fracture detection is a crucial part of radiological diagnostics. Automating this process helps reduce human error and speeds up medical response. This project uses transfer learning to achieve high accuracy with minimal training time.

---

## 📁 Dataset

- **Source:** Kaggle
- **Structure:**
  - `train/`
  - `val/`
  - `test/`
  - Each contains 2 folders: `Comminuted Bone Fracture`, `Simple Bone Fracture`
- Includes both **original** and **augmented** images.

---

## 🛠️ Tech Stack

- **Python**
- **TensorFlow / Keras**
- **MobileNetV2**
- **Streamlit**
- **Google Colab**
- **Matplotlib, NumPy, Pandas**
- **Image Augmentation (ImageDataGenerator)**

---

## 🚀 How It Works

1. The model is trained using `MobileNetV2` pre-trained on ImageNet.
2. Input images are preprocessed and passed to the model.
3. The app predicts the class and displays the confidence for each.
4. Built with an easy-to-use **Streamlit web interface**.

---

## 📷 App Screenshot

![App Screenshot](screenshot.png)


---

## 📈 Results

- **Training Accuracy:** 97%
- **Validation Accuracy:** 93%
- **Test Accuracy:** 92.8%

---

## 📌 Author

**Israa Khamis**  
AI Engineer | Machine Learning | Deep Learning   
📎 [LinkedIn](https://www.linkedin.com/in/https://www.linkedin.com/in/israa-khamis-0bb7ba365) • [GitHub](https://github.com/(https://github.com/israakhamis2545))

---

## 💬 Acknowledgements

Thanks to **Kaggle** for the dataset and **NTI AI Track** for the inspiration.


