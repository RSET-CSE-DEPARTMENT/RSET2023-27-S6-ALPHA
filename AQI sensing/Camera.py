import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os
# 👇 NEW: Importing the official MobileNetV2 translator
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

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
    st.write("Upload a photo or point your camera at the sky to estimate air quality visually.")

    if model is None:
        return

    st.markdown("---")

    # 👇 NEW: Let the user choose between Camera and Upload
    input_method = st.radio("Choose Input Method:", ["📁 Upload an Image", "📸 Use Webcam"])
    
    # Create a variable to hold the final image source
    image_source = None

    if input_method == "📸 Use Webcam":
        image_source = st.camera_input("Take a picture of the environment")
    else:
        image_source = st.file_uploader("Upload a landscape or sky photo", type=["jpg", "jpeg", "png"])

    # If the user has provided an image (either via camera or upload)
    if image_source is not None:
        st.write("🧠 AI is analyzing...")
        
        # 4. Prepare the image
        # Open and convert to standard RGB (fixes the "Red Sky" bug)
        image = Image.open(image_source).convert('RGB')
        
        # Display the image they are testing on screen so you can verify it
        st.image(image, caption="Image to Analyze", use_container_width=True)

        # Squash to 224x224
        image = image.resize((224, 224)) 
        
        # Convert to an array of decimals (float32)
        img_array = np.array(image, dtype=np.float32)
        
        # 👇 NEW: Use the official MobileNetV2 math translator instead of "/ 255.0"
        img_array = preprocess_input(img_array)
        
        # Add the batch dimension
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