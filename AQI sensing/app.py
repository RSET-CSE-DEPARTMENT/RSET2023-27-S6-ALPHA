import streamlit as st
import Comparison
import Simulation
import RealTime
import Camera  # This links to your Camera.py file

st.set_page_config(page_title="AQI Prediction System", layout="wide")

st.title("🌍 AQI Prediction System")

st.sidebar.title("Navigation")

# Added "Camera AI" to the selection
choice = st.sidebar.radio(
    "Select Mode",
    ["Comparison", "Simulation", "Real-Time", "Camera AI"]
)

# -----------------------------
# Module Switching
# -----------------------------
if choice == "Comparison":
    Comparison.run()

elif choice == "Simulation":
    Simulation.run()

elif choice == "Real-Time":
    RealTime.run()

elif choice == "Camera AI":
    # This calls the run() function inside your Camera.py
    Camera.run()