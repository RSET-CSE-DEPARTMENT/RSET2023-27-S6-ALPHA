import streamlit as st
import serial
import time
import pandas as pd
import joblib

def run():

    st.title("🔴 Real-Time AQI Monitoring")
    st.write("Listening for live sensor data from Arduino...")

    # --------------------------
    # Load AI Model
    # --------------------------
    @st.cache_resource
    def load_model():
        try:
            return joblib.load("aqi_model.pkl")
        except:
            return None

    model = load_model()

    if model is None:
        st.error("⚠️ Model file 'aqi_model.pkl' not found.")
        return

    # --------------------------
    # Hardware Connection UI
    # --------------------------
    st.markdown("### 🔌 Hardware Connection")

    com_port = st.text_input(
        "Arduino COM Port:",
        value="COM7"
    )

    start = st.button("📡 Start Live Feed")

    if start:

        try:
            ser = serial.Serial(com_port, 9600, timeout=1)

            st.success(f"Connected to {com_port}")

            time.sleep(2)

            ui = st.empty()

            while True:

                try:
                    line = ser.readline().decode("utf-8").strip()

                    if not line:
                        continue

                    data = line.split(",")

                    if len(data) != 3:
                        continue

                    pm25 = float(data[0])
                    co = float(data[1])
                    nh3 = float(data[2])

                    # --------------------------
                    # Predict AQI
                    # --------------------------
                    input_df = pd.DataFrame(
                        [[pm25, co, nh3]],
                        columns=["PM2.5", "CO", "NH3"]
                    )

                    aqi = int(model.predict(input_df)[0])

                    # --------------------------
                    # AQI Category
                    # --------------------------
                    if aqi <= 50:
                        status = "GOOD"
                        color = "green"

                    elif aqi <= 100:
                        status = "SATISFACTORY"
                        color = "yellow"

                    elif aqi <= 200:
                        status = "MODERATE"
                        color = "orange"

                    else:
                        status = "HAZARDOUS"
                        color = "red"

                    # --------------------------
                    # Display
                    # --------------------------
                    with ui.container():

                        st.markdown("---")

                        st.markdown(
                            f"<h1 style='text-align:center;color:{color};'>AQI: {aqi}</h1>",
                            unsafe_allow_html=True
                        )

                        st.markdown(
                            f"<h3 style='text-align:center;color:{color};'>{status}</h3>",
                            unsafe_allow_html=True
                        )

                        col1, col2, col3 = st.columns(3)

                        col1.metric(
                            "PM2.5",
                            f"{pm25:.2f} µg/m³"
                        )

                        col2.metric(
                            "CO",
                            f"{co:.2f} ppm"
                        )

                        col3.metric(
                            "NH3",
                            f"{nh3:.2f} ppm"
                        )

                except:
                    pass

        except:
            st.error(
                "❌ Could not connect.\n\n"
                "Make sure:\n"
                "- Arduino is plugged in\n"
                "- COM port is correct\n"
                "- Arduino IDE Serial Monitor is CLOSED"
            )