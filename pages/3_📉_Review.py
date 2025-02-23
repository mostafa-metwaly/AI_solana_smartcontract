import streamlit as st

st.set_page_config(
    page_title="Review",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="collapsed"
)


############ REVIEW PHOTO #############

st.subheader("Contract detail")

st.write(f"Price is {st.session_state.get('price', 'not defined')}")
st.write(f"Time is {st.session_state.get('time', 'not defined')}")
st.write(f"Job comment is {st.session_state.get('job_comment', 'not defined')}")

st.divider()

if "freelancer_photo" in st.session_state:
    st.subheader("Freelancer photo")
    st.image(st.session_state["freelancer_photo"], caption="Freelancer photo")
    st.write("AI analysis")
    st.json(st.session_state["wedding_evaluation"])

# st.divider()

############ APPROVE PHOTO #############

# st.subheader("Final")
# st.write("Please review your photo carefully. If you *approve the work*, the contract will complete and all funds will be transfered. If you *dispute the work* our AI assistent will make a judgement for both parties.")


# aprove work (session state)
# if 'clicked' not in st.session_state:
#     st.session_state.clicked = False

# def click_button():
#     st.session_state.clicked = True

# st.button(
#     'Approve work',
#     on_click=click_button,
#     )

# if st.session_state.clicked:
#     # The message and nested widget will remain on the page
#     st.write("Your contract has been executed! 🎉")

# # dispute work
# if st.button("Dispute work"):
#     st.write("")
#     st.write("Visit the *Judge* page to view your results. ⛔️")