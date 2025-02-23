import streamlit as st
from deepface import DeepFace

verify_url = "https://mostafa.duck-alpheratz.ts.net/verify"

st.set_page_config(
    page_title="Customer",
    page_icon="👰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

############# UPLOAD CUSTOMER PHOTO  #############

st.subheader("Personal photo")
st.write("This photo allows AI to ensure the quality of your final product.")

st.divider()

photo_key = "customer_photo"

if photo_key not in st.session_state:
    st.session_state[photo_key] = None

uploaded_file = st.file_uploader(
    "Upload an image", type=["png", "jpg", "jpeg"])


if uploaded_file is not None:
    image_bytes = uploaded_file.read()
    st.session_state[photo_key] = image_bytes  # Store it persistently

if st.session_state[photo_key]:
    st.image(st.session_state[photo_key], caption="Uploaded Image")


    # Provide an 'Verify' button for each image.

    if st.button("Verify Matching"):
        # Encode the image.
        # print(st.session_state["customer_photo"])
        # print(st.session_state["freelancer_photo"])
        
        with open("pages/freelancer_photo.jpg", "wb") as f:
            f.write(st.session_state["freelancer_photo"]) 

        with open("pages/customer_photo.jpg", "wb") as f:
            f.write(st.session_state["customer_photo"])     
        st.session_state["user_verification"]  = DeepFace.verify(img1_path = "C:\\Users\\uditp\\MenteruNewTask\\Solana_multiSig_contract\\app\\pages\\customer_photo.jpg",
                                                                 img2_path = "C:\\Users\\uditp\\MenteruNewTask\\Solana_multiSig_contract\\app\\pages\\freelancer_photo.jpg", 
                                                                 model_name='Facenet512',
                                                                 distance_metric='cosine')

        
        st.json(st.session_state["user_verification"])
        
# request:
# {
#     "img1": "https://cdn.discordapp.com/attachments/1342463644432207892/1342778836130992198/img1.jpeg?ex=67bb887e&is=67ba36fe&hm=e554fb3f70adbb5dd7198b92423b9071c1dffe41e11e0ca7bebb812721781536&",
#     "img2": "https://jammulinksnews.com/admin_panel/media/semi/490654992024506490.jpg",
#     "model_name": "DeepFace",
#     "detector_backend": "opencv",
#     "distance_metric": "euclidean"
# }


# response:
# {"detector_backend": "opencv", "distance": 53.80508539135102, "facial_areas": {"img1": {"h": 541, "left_eye": [925, 403], "right_eye": [748, 401], "w": 541, "x": 573, "y": 175}, "img2": {
#     "h": 216, "left_eye": [463, 172], "right_eye": [384, 167], "w": 216, "x": 312, "y": 80}}, "model": "DeepFace", "similarity_metric": "euclidean", "threshold": 64, "time": 2.52, "verified": true}


# ############# CONTRACT REVIEW #############

# st.subheader("Sign smart contract")

# # freelancer price
# st.write("**Solana price:**")
# st.write("{PASS VARIABLE}")

# # freelancer time
# st.write("**Delivered in:**")
# st.write("{PASS VARIABLE}")

# # freelancer comments
# st.write("**Freelancer comments:**")
# st.write("{PASS VARIABLE}")

# ### SIGN CONTRACT (BTN)

# if 'clicked' not in st.session_state:
#     st.session_state.clicked = False

# def click_button():
#     st.session_state.clicked = True

# st.button('Sign contract', on_click=click_button)

# if st.session_state.clicked:
#     # The message and nested widget will remain on the page
#     st.write('Contract signed!')

