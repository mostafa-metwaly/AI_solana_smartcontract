import streamlit as st

st.set_page_config(
    page_title="Customer",
    page_icon="👰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

############# UPLOAD CUSTOMER PHOTO  #############

st.subheader("Personal photo")
st.write("This photo allows AI to ensure the quality of your final product.")

#### UPLOAD PIC
st.file_uploader(
    "Upload one photo below:",
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

st.divider()


############# CONTRACT REVIEW #############

st.subheader("Sign smart contract")

# freelancer price
st.write("**Solana price:**")
st.write("{PASS VARIABLE}")

# freelancer time
st.write("**Delivered in:**")
st.write("{PASS VARIABLE}")

# freelancer comments
st.write("**Freelancer comments:**")
st.write("{PASS VARIABLE}")

### SIGN CONTRACT (BTN)

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Sign contract', on_click=click_button)

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write('Contract signed!')

