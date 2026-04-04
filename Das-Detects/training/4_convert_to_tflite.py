
import tensorflow as tf
from tensorflow import keras
import os
import sys
from pathlib import Path

# Add current directory to path so we can import models/config
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import config
from models.layers import DepthwiseSeparableConv2D, ConvBlock

def convert_to_tflite(model_path, output_path, quantization='float32'):
    """
    Convert Keras model to TFLite.
    
    Args:
        model_path: Path to .keras model
        output_path: Path to save .tflite model
        quantization: 'float32', 'dynamic', or 'float16'
    """
    if not os.path.exists(model_path):
        print(f"Error: Model not found at {model_path}")
        return

    print(f"Loading model from {model_path}...")
    try:
        model = keras.models.load_model(
            model_path, 
            custom_objects={
                'DepthwiseSeparableConv2D': DepthwiseSeparableConv2D,
                'ConvBlock': ConvBlock
            }
        )
    except Exception as e:
        print(f"Failed to load model: {e}")
        return

    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    
    if quantization == 'dynamic':
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
    elif quantization == 'float16':
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        converter.target_spec.supported_types = [tf.float16]
        
    print(f"Converting model (quantization: {quantization})...")
    tflite_model = converter.convert()
    
    with open(output_path, 'wb') as f:
        f.write(tflite_model)
        
    size_kb = len(tflite_model) / 1024
    print(f"Saved TFLite model to {output_path}")
    print(f"Size: {size_kb:.2f} KB")

if __name__ == "__main__":
    # Default paths
    MODEL_DIR = r"D:\datasets\models_mel_custom_v5"
    KERAS_MODEL = os.path.join(MODEL_DIR, "best_model.keras")
    TFLITE_MODEL = os.path.join(MODEL_DIR, "voice_classifier_v5.tflite")
    
    convert_to_tflite(KERAS_MODEL, TFLITE_MODEL)
