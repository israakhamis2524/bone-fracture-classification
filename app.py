import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

model = load_model("bone_model.keras")
class_names = ['Comminuted Bone Fracture', 'Simple Bone Fracture']

st.title("Bone Fracture Classification")

uploaded_file = st.file_uploader("Upload an X-ray image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded X-ray", use_column_width=True)

    img = image.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    st.subheader("Prediction:")
    st.write(predicted_class)

    st.subheader("Confidence:")
    for i, prob in enumerate(prediction[0]):
        st.write(f"{class_names[i]}: {prob * 100:.2f}%")