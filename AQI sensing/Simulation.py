import streamlit as st

def run():
    import time
    import pandas as pd
    import numpy as np
    import joblib

    # -------------------------------
    # LOAD MODEL ONLY ONCE
    # -------------------------------
    if "simulation_model" not in st.session_state:
        try:
            st.session_state.simulation_model = joblib.load("aqi_model.pkl")
        except Exception:
            st.session_state.simulation_model = None

    model = st.session_state.simulation_model

    # -------------------------------
    # UI
    # -------------------------------
    st.title("☁️ Urban Air Quality: Sky-Fusion System")
    st.markdown("**Mode:** <span style='color:green'>Simulation (Manual Test)</span>", unsafe_allow_html=True)
    st.write("Enter chemical sensor values to predict AQI using Gradient Boosting.")

    if model is None:
        st.error("⚠️ Model not found! Please make sure 'aqi_model.pkl' is in same folder.")
        return

    st.markdown("---")

    st.markdown('<div style="padding:10px;border-radius:5px;background-color:#1E2A40;color:#4caf50;border-left:5px solid #4caf50;">🧪 Chemical Domain (Simulation)</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        pm25 = st.number_input("PM2.5 (µg/m³)", value=110.0, step=1.0)

    with col2:
        co_level = st.number_input("CO (ppm)", value=12.5, step=0.1)

    with col3:
        nh3_level = st.number_input("NH3 (µg/m³)", value=45.0, step=1.0)

    st.markdown("<br>", unsafe_allow_html=True)

    # -------------------------------
    # PREDICTION
    # -------------------------------
    if st.button("🚀 CALCULATE AQI"):

        with st.spinner("Analyzing pollutant concentrations..."):
            time.sleep(0.5)

            input_df = pd.DataFrame(
                [[pm25, co_level, nh3_level]],
                columns=['PM2.5', 'CO', 'NH3']
            )

            predicted_aqi = int(model.predict(input_df)[0])

        st.subheader("📊 Gradient Boosting Analysis Results")

        colA, colB = st.columns([1, 2])

        with colA:
            st.metric("Predicted AQI", predicted_aqi)

        with colB:
            if predicted_aqi <= 50:
                status = "GOOD 🟢"
            elif predicted_aqi <= 100:
                status = "SATISFACTORY 🟡"
            elif predicted_aqi <= 200:
                status = "MODERATE 🟠"
            else:
                status = "POOR / HAZARDOUS 🔴"

            st.success(f"Status: {status}")

        # Simulated trend
        st.subheader("📈 Simulated Pollutant Trends (Last 24 Hrs)")

        hours = [f"{i}:00" for i in range(24)]

        trend_data = pd.DataFrame({
            "PM2.5": np.random.normal(pm25, 15, 24),
            "CO": np.random.normal(co_level, 2, 24),
            "NH3": np.random.normal(nh3_level, 10, 24)
        }, index=hours)

        trend_data = trend_data.clip(lower=0)

        st.line_chart(trend_data)
