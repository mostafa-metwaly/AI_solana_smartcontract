import streamlit as st

st.set_page_config(
    page_title="Results",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="collapsed"
)


############ REVIEW PHOTO #############

st.subheader("Review your photo")

# TEMP IMAGE!!!!
st.image(
    "wedding.jpeg",
    caption="Review the quality of your photo!",
    use_container_width=True
    )

st.divider()

############ APPROVE PHOTO #############

st.subheader("Approve work")
st.write("Please review your photo carefully. If you *approve the work*, the contract will complete and all funds will be transfered. If you *dispute the work* our AI assistent will make a judgement for both parties.")


# aprove work (session state)
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button(
    'Approve work',
    on_click=click_button,
    )

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write("Your contract has been executed! 🎉")

# dispute work
if st.button("Dispute work"):
    st.write("")
    st.write("Visit the *Judge* page to view your results. ⛔️")