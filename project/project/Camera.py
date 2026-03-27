import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

def run():
    # 1. Load the AI Brain
    @st.cache_resource
    def load_ai_model():
        current_folder = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_folder, 'camera_aqi_model.keras')
        
        if not os.path.exists(model_path):
            st.error(f"❌ Model file not found at: {model_path}")
            return None
            
        try:
            # compile=False is the key to bypassing version conflicts
            return tf.keras.models.load_model(model_path, compile=False)
        except Exception as e:
            st.error(f"🛑 Error loading model: {e}")
            return None

    model = load_ai_model()

    # 2. Define Categories
    CLASS_NAMES = [
        "Good (0-50) 🟢", 
        "Moderate (51-100) 🟡", 
        "Unhealthy for Sensitive Groups (101-150) 🟠", 
        "Unhealthy (151-200) 🔴", 
        "Very Unhealthy (201-300) 🟣", 
        "Severe (301+) 🟤"
    ]

    st.title("📷 AI Camera AQI Detector")
    st.write("Point your camera at the sky to estimate air quality visually.")

    if model is None:
        return

    st.markdown("---")

    # 3. Open the laptop webcam
    camera_photo = st.camera_input("Take a picture of the environment")

    if camera_photo is not None:
        st.write("🧠 AI is analyzing...")
        
        # 4. Prepare the image
        image = Image.open(camera_photo).convert('RGB')
        image = image.resize((224, 224)) 
        img_array = np.array(image) / 255.0  # Normalize to match MobileNetV2
        img_array = np.expand_dims(img_array, axis=0) 

        # 5. Prediction
        predictions = model.predict(img_array)
        predicted_index = np.argmax(predictions[0])
        confidence = np.max(predictions[0]) * 100
        predicted_label = CLASS_NAMES[predicted_index]

        # 6. Results
        st.subheader("📊 Results")
        st.success(f"**Predicted Air Quality:** {predicted_label}")
        st.info(f"**AI Confidence:** {confidence:.2f}%")