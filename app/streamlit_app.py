import streamlit as st

from manual_input import render_manual_input
from json_input import render_json_input

st.title("Mesh Quality Classification")

st.write(
    "Predict mesh quality class using "
    "geometric and topological features."
)

input_method = st.radio(
    "Choose input method:",
    [
        "Upload OBJ model",
        "Upload JSON features",
        "Manual input"
    ]
)

st.write(f"Selected method: {input_method}")

if input_method == "Manual input":
    render_manual_input()

elif input_method == "Upload JSON features":
    render_json_input()

elif input_method == "Upload OBJ model":
    st.info("OBJ upload will be later.")