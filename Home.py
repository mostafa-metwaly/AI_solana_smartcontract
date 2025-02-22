import streamlit as st

st.set_page_config(
    page_title="Builders Weekend",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# sidebar helper
st.sidebar.success("Select a page above")
#product name variable
productName = "ConVeni"

############# SESSION STATE #############

# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'



############# WELCOME #############
st.subheader(f"Welcome to {productName}! 🏪")

st.write(f"{productName} (convenience contracts) utilize artificial intelligence and blockchain technologies to promote fairer contracts between freelancers and their clients. **With our product users:**")

# FEATURE LIST
st.markdown("- Can make payments conveniently with solara tokens 🚀")
st.markdown("- Can confidently cancel contracts, and receive refunds ⏳")
st.markdown("- Don't worry about deposits negotiations or timelines 💰")
st.markdown("- No longer require litigation to handle quality disputes 🧑🏼‍⚖️")

# bullet styling (for above)
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
    margin-top: 0;
    line-height: 0.5;
}
</style>
''', unsafe_allow_html=True)

# margin hack
st.write("")
st.write("")

############# CONTRACT DETAILS #############

# UTILIZE FORM TO SUBMIT
with st.form("my_form"):
    
    st.subheader("Define your smart contract:")
    
    # job price
    price = st.slider("💰 Solana coins required:", 1, 10)
    
    # job duration
    time = st.selectbox(
    "⏱️ Time required to complete service:",
    ("3 day", "5 days", "7 days"),
    index=None,
    placeholder="Days required"
    )
    st.write("You selected:", time)
    
    # job comments
    comments = st.text_input("💬 Additional comments for customer:")

    # submit button
    st.form_submit_button('Submit proposal')










# ############ CONTRACT STATUS #############

# st.subheader("Contract Progress")
# st.button("Freelancer", type="primary")
# st.button("Customer", type="secondary")


# #### DYNAMIC BUTTON

# # st.button("Reset", type="primary")
# # if st.button("Say hello"):
# #     st.write("Why hello there")
# # else:
# #     st.write("Goodbye")

# # if st.button("Aloha", type="tertiary"):
# #     st.write("Ciao")


# # Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "App navigation",
#     ("Freelancer", "Customer", "Results")
# )

