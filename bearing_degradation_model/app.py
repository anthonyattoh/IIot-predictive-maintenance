import streamlit as st
import joblib
import numpy as np

model = joblib.load('bearing_degradation_model/bearing_model.pkl')
st.title("Bearing Degradation Predictor")
st.write("Enter recent sensor readings to estimate Remaining Useful Life (RUL)")

feature_names = ['sensor_2', 'sensor_3', 'sensor_4', 'sensor_7', 'sensor_8', 'sensor_9',
                  'sensor_11', 'sensor_12', 'sensor_13', 'sensor_14', 'sensor_15',
                  'sensor_17', 'sensor_20', 'sensor_21']

inputs = []
for name in feature_names:
    value = st.number_input(f"{name} (5-cycle rolling average)", value=0.0)
    inputs.append(value)

if st.button("Predict RUL"):
    try:
        X = np.array(inputs).reshape(1, -1)
        prediction = model.predict(X)[0]

        st.metric("Predicted Remaining Useful Life", f"{prediction:.0f} cycles")

        if prediction < 30:
            st.error("Critical - schedule maintenance soon")
        elif prediction < 60:
            st.warning("Degrading - monitor closely")
        else:
            st.success("Healthy")

    except Exception as e:
        st.error(f"Couldn't generate a prediction - please check that all sensor values are valid numbers. ({e})")
