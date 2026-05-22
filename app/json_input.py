import json

import streamlit as st
import requests

from utils import display_prediction_results


def render_json_input():

    st.subheader("Upload JSON file")

    uploaded_file = st.file_uploader(
        "Choose a JSON file",
        type=["json"]
    )

    if uploaded_file is not None:

        if st.button("Predict from JSON"):

            try:

                json_data = uploaded_file.getvalue()

                payload = json.loads(
                    json_data
                )

                response = requests.post(
                    "http://127.0.0.1:8000/predict",
                    json=payload,
                    timeout=10
                )

                response.raise_for_status()

                prediction = response.json()

                display_prediction_results(
                    prediction,
                    payload
                )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to FastAPI server."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "Request timed out."
                )

            except requests.exceptions.HTTPError:

                st.error(
                    f"HTTP error: {response.status_code}"
                )

            except json.JSONDecodeError:

                st.error(
                    "Invalid JSON file."
                )

            except Exception as e:

                st.error(
                    f"Unexpected error: {e}"
                )