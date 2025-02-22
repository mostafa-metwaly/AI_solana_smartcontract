import streamlit as st

st.set_page_config(
    page_title="Judge",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# bullet styling (for above)
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] p{
    margin-top: 0;
    line-height: 0.9;
}
</style>
''', unsafe_allow_html=True)

############ REVIEW PHOTO #############

### GET STORED IMAGE
st.subheader("AI Judge Results")

st.image(
    "wedding.jpeg",
    caption="Your photo has been reviewed.",
    )

### FACIAL RECOGNITION (RESULTS)
st.write("**Genuine Photo Rating:**")

# scenario (A)
st.write("AI has determined this is a picture of you, with a {VARIABLE} confidence level. ✅")

# scenario (B)
# st.write("AI has determined that this is NOT a geniune photo, with a {VARIABLE} confidence level. ⛔️")


### WEDDING PHOTO (TRUE/FALSE)
st.markdown("") # padding hack
st.markdown("**Photo Quality Rating:**")

# scenario (A)
st.write("AI has determined this is a high-quality wedding photo. ✅")

# scenario (B)
# st.write("AI has determined that this is NOT a high-quality wedding photo. ⛔️")

### WEDDING PHOTO (EXPLANATION)
st.write("{EXPLANATION FROM LLM}")


st.divider()

############ DETERMINATION #############

st.subheader("Determination")

# scenario (A)
st.write("Your contract has been executed, and your coins have been exchanged. 🤝")

# scenario (B)
# st.write("Your contract has been cancelled, and your coins have been refunded. 🔁")
