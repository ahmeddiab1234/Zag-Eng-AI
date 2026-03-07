import streamlit as st
import pandas as pd
import requests
import io

API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="NYC Trip Duration Prediction",
    layout="centered"
)

st.title("NYC Trip Duration Prediction")
tab1, tab2 = st.tabs(["Single Prediction", "CSV Prediction"])

with tab1:
    st.subheader("Predict Single Trip Duration")

    vendor_id = st.selectbox("Vendor ID", [1, 2])
    pickup_datetime = st.text_input(
        "Pickup Datetime (YYYY-MM-DD HH:MM:SS)",
        value="2016-01-01 08:30:00"
    )
    passenger_count = st.number_input("Passenger Count", min_value=1, max_value=10, value=1)
    pickup_longitude = st.number_input("Pickup Longitude", value=-73.9857, format="%.6f")
    pickup_latitude = st.number_input("Pickup Latitude", value=40.7484, format="%.6f")
    dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.9851, format="%.6f")
    dropoff_latitude = st.number_input("Dropoff Latitude", value=40.7580, format="%.6f")
    store_and_fwd_flag = st.selectbox("Store & Forward Flag", ["N", "Y"])

    if st.button("Predict Trip Duration"):
        payload = {
            "vendor_id": vendor_id,
            "pickup_datetime": pickup_datetime,
            "passenger_count": passenger_count,
            "pickup_longitude": pickup_longitude,
            "pickup_latitude": pickup_latitude,
            "dropoff_longitude": dropoff_longitude,
            "dropoff_latitude": dropoff_latitude,
            "store_and_fwd_flag": store_and_fwd_flag
        }

        try:
            response = requests.post(f"{API_URL}/predict", json=payload)

            if response.status_code == 200:
                result = response.json()
                seconds = result["trip_duration_prediction"]
                minutes = seconds / 60

                st.success(f"Predicted Trip Duration: **{seconds:.2f} seconds**")
                st.info(f"≈ {minutes:.2f} minutes")

            else:
                st.error(response.text)

        except Exception as e:
            st.error(f"API Error: {e}")

with tab2:
    st.subheader("Predict Trip Duration from CSV")

    st.markdown(
        """
        **Required columns:**
        - vendor_id
        - pickup_datetime
        - passenger_count
        - pickup_longitude
        - pickup_latitude
        - dropoff_longitude
        - dropoff_latitude
        - store_and_fwd_flag
        """
    )

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        st.write("Preview:")
        df_preview = pd.read_csv(uploaded_file)
        st.dataframe(df_preview.head())

        if st.button("Predict CSV"):
            try:
                files = {
                    "file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")
                }

                response = requests.post(
                    f"{API_URL}/predict_csv",
                    files=files
                )

                if response.status_code == 200:
                    result_df = pd.read_csv(io.StringIO(response.text))
                    st.success("Prediction completed")

                    st.dataframe(result_df.head())

                    csv = result_df.to_csv(index=False).encode("utf-8")
                    st.download_button(
                        "Download Predictions CSV",
                        csv,
                        file_name="predictions.csv",
                        mime="text/csv"
                    )
                else:
                    st.error(response.text)

            except Exception as e:
                st.error(f"API Error: {e}")



st.markdown("""
<style>
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
