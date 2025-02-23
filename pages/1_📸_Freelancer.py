from io import BytesIO
import json
import time
import requests
import streamlit as st
import os
import base64
from utils import encode_bytes_to_base64, encode_image_to_base64, decode_base64_to_bytes

ollama_url = "https://dellpro.goose-royal.ts.net/api/generate"
ollama_retries = 5



def clean_response(response_text: str):
    # Remove markdown code block markers if present
    cleaned_response_text = response_text.strip()
    if cleaned_response_text.startswith("```json"):
        cleaned_response_text = cleaned_response_text[len(
            "```json"):].strip()
    if cleaned_response_text.endswith("```"):
        cleaned_response_text = cleaned_response_text[:-3].strip()
    return cleaned_response_text



def get_ollama_evaluation(encoded_image: str) -> dict:
    """
    Evaluate if an image is a wedding picture or not
    """
    # Define the prompt.
    prompt = """Is it a wedding picture?
        Answer in json, with the following structure:
        {
            "answer": "yes" | "no",
            "explanation": your reasoning,
            "confidence": rate from 0 to 10 how sure you are about your yes|no answer
        }
        """
    # Prepare the payload.
    payload = {
            "model": "llava:7b",
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "images": [encoded_image]
            }
    headers = {
        "Host": "127.0.0.1:11434",  # local service expects this host header
        "Origin": "http://127.0.0.1"
        }

    for attempt in range(ollama_retries):
        try:
            response = requests.post(
                ollama_url, json=payload, headers=headers)
            response.raise_for_status()  # Raises HTTPError for bad responses
            response_data = response.json()
            cleaned_response = clean_response(
                response_data.get("response", ""))
            evaluation = json.loads(cleaned_response)
            break
        except (requests.RequestException, json.JSONDecodeError) as e:
            if attempt < ollama_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                evaluation = {
                    "answer": "error",
                    "explanation": f"Failed after {ollama_retries} attempts: {str(e)}",
                    "confidence": 0
                }
    return evaluation


st.set_page_config(
    page_title="Freelancer",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.subheader("Finished project?")


photo_key = "freelancer_photo"

if photo_key not in st.session_state:
    st.session_state[photo_key] = None

uploaded_file = st.file_uploader(
    "Upload an image", type=["png", "jpg", "jpeg"])


if uploaded_file is not None:
    image_bytes = uploaded_file.read()
    st.session_state[photo_key] = image_bytes  # Store it persistently
    
if st.session_state[photo_key]:
    st.image(st.session_state[photo_key], caption="Uploaded Image", width=600)
    
    # Provide an 'Analyze' button for each image.
    if st.button("Submit"):
        # Encode the image.

        encoded = encode_bytes_to_base64(st.session_state[photo_key])
        
        st.session_state["wedding_evaluation"] = get_ollama_evaluation(encoded)
        
        st.json(st.session_state["wedding_evaluation"])

# if "freelancer_uploaded_file" in st.session_state:
    
#     st.write(f"freelancer has uploaded files")
    
#     print(st.session_state.freelancer_uploaded_file)
    
#     os.makedirs("uploads", exist_ok=True)
#     # Loop through each uploaded file.
#     for (i, uploaded_file) in enumerate(st.session_state.freelancer_uploaded_file):
        
#         # Save file to disk.
#         save_path = os.path.join("uploads", uploaded_file.name)
#         with open(save_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())
            
#         # Save encoded image to session
#         encoded = encode_image_to_base64(save_path)
#         st.session_state[f"wedding_{i}"] = encoded
        
#         st.image(decode_base64_to_bytes(
#             st.session_state[f"wedding_{i}"]), caption=uploaded_file.name, use_container_width=True)

#         # # Display the image with a caption.
#         # st.image(save_path, caption=uploaded_file.name,
#         #          use_container_width=True)

#         # Provide an 'Analyze' button for each image.
#         if st.button("Analyze", key=f"analyze_{uploaded_file.name}"):
#             # Encode the image.

#             evaluation = get_ollama_evaluation(encoded)
                        
#             st.json(evaluation)


# # Optional: a global "Submit work" button if needed for additional workflow.
# if 'submitted' not in st.session_state:
#     st.session_state.submitted = False


# def submit_work():
#     st.session_state.submitted = True


# if st.button("Submit work"):
#     submit_work()

# if st.session_state.submitted:
#     st.write("Work submitted!")
