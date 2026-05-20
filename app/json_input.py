import streamlit as st
import requests


def render_json_input():

    st.subheader("Upload JSON file")

    uploaded_file = st.file_uploader(
        "Choose a JSON file",
        type=["json"]
    )

    if uploaded_file is not None:

        json_data = uploaded_file.read()

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            data=json_data,
            headers={"Content-Type": "application/json"}
        )

        prediction = response.json()

        st.success(
            f"Predicted quality class: "
            f"{prediction['predicted_quality_class']}"
        )