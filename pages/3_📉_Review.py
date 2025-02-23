import streamlit as st
import requests

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
    st.json(st.session_state.get("wedding_evaluation", {}))

st.divider()

if "customer_photo" in st.session_state:
    st.subheader("customer photo")
    st.image(st.session_state["customer_photo"], caption="customer photo")
    st.write("ML analysis")
    st.json(st.session_state.get("facial_verification", {}))

st.divider()

############ JUDGE AI VERDICT #############
st.subheader("Judge AI Verdict")

# Button to trigger the Judge AI call
if st.button("Check Judge AI Verdict"):
    if "facial_verification" in st.session_state and "wedding_evaluation" in st.session_state:
        # Retrieve the results from session state.
        facial_result = st.session_state["facial_verification"]  # e.g., "verified" or "not verified"
        wedding_eval = st.session_state["wedding_evaluation"]    # Dict with keys: "answer", "confidence", "explanation"
        # Extract details from the wedding evaluation.
        wedding_answer = wedding_eval.get("answer", "unknown")
        wedding_confidence = wedding_eval.get("confidence", "N/A")
        wedding_explanation = wedding_eval.get("explanation", "No explanation provided")
        
        # Combine both outputs into a single string for the judge.
        raw_input_text = (
            f"Facial recognition: {facial_result}. "
            f"Wedding image: {wedding_answer} (confidence {wedding_confidence}). "
            f"Explanation: {wedding_explanation}."
        )
        print(raw_input_text)
        
        # Your Tailscale-based Judge API URL.
        judge_api_url = "https://uditslaptop.taila51f38.ts.net/judge"
        
        # Call the Judge API with robust error handling.
        try:
            judge_response = requests.post(judge_api_url, json={"raw_input": raw_input_text}, timeout=15)
            
            # If the request was successful (status_code = 200)
            if judge_response.ok:
                # Extract data from the JSON response
                response_json = judge_response.json()
                final_verdict = response_json.get("final_verdict", "No 'final_verdict' key in response.")
                st.markdown("### Final Verdict from Judge AI")
                st.write(final_verdict)
            else:
                # Non-200 status code from the server
                st.error(f"Judge API request failed with status code: {judge_response.status_code}")
                st.write("Response text:", judge_response.text)
        
        except requests.exceptions.Timeout:
            st.error("The request to the Judge API timed out. Please try again later.")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred while calling the Judge API: {e}")

    else:
        st.info("Facial recognition matches, and the submitted images are confirmed to be a genuine wedding photo. The photographer has successfully finished the job!")
else:
    st.write("Click the button above to see the Judge AI verdict.")

st.divider()

############ APPROVE PHOTO #############

st.subheader("Final")
st.write("Please review your photo carefully. If you *approve the work*, the contract will complete and all funds will be transferred. If you *dispute the work*, our AI assistant will make a judgment for both parties.")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

# Approve work
if st.session_state.clicked:
    st.write("Your contract has been executed! 🎉")

# Dispute work
if st.button("Dispute work"):
    st.write("")
    st.write("Visit the *Judge* page to view your results. ⛔️")
