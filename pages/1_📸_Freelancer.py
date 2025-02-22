import requests
import streamlit as st
import os
# import pandas as pd
# from io import StringIO

import base64

BACKEND_URL = "http://127.0.0.1:5000/upload"


def encode_image_to_base64(image_path):
    """
    Reads an image file and encodes it as a base64 string.
    
    Parameters:
    - image_path (str): Path to the image file.

    Returns:
    - str: Base64-encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

st.set_page_config(
    page_title="Freelancer",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

############# UPLOAD AND SUBMIT #############

st.subheader("Finished project?")

#### UPLOAD PIC
uploaded_file = st.file_uploader(
    "Upload one photo:",
    type=None,
    accept_multiple_files=False,
    key=None,
    help=None,
    on_change=None,
    args=None,
    kwargs=None,
    disabled=False,
    label_visibility="visible",
    )

if uploaded_file is not None:
    # Save file to disk
    save_path = os.path.join("uploads", uploaded_file.name)
    os.makedirs("uploads", exist_ok=True)  # Ensure directory exists

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    encoded = encode_image_to_base64(save_path)

    st.success(f"File saved: {save_path}")
    st.success(f"Encoded image is:\n{encoded}")
    
    # response = requests.post(
    #     BACKEND_URL, json={"image": encoded, "filename": uploaded_file.name})

    #    if response.status_code == 200:
    #         st.success("Image successfully sent to backend!")
    #     else:
    #         st.error("Failed to send image to backend.")

### SIGN CONTRACT (BTN)

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Submit work', on_click=click_button)

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write('Work submitted!')