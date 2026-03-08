import streamlit as st
import requests

# Backend API URL
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="AI Exam Anxiety Detector", page_icon="🧠", layout="centered")

st.title("🧠 AI Based Exam Anxiety Detector")
st.write("Enter your thoughts or feelings about an upcoming exam, and our AI will detect your anxiety level.")

# Text input for the user
user_input = st.text_area("How are you feeling about your exams?", height=150, placeholder="e.g., I can't sleep because I am so worried about my math exam tomorrow.")

if st.button("Detect Anxiety Level"):
    if not user_input.strip():
        st.warning("Please enter some text before analyzing.")
    else:
        with st.spinner("Analyzing..."):
            try:
                # Send request to backend
                payload = {"text": user_input}
                response = requests.post(API_URL, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    anxiety_level = result.get("anxiety_level", "Unknown")
                    confidence = result.get("confidence", 0.0)
                    
                    # Display results with different colors based on anxiety level
                    st.subheader("Analysis Result:")
                    
                    if anxiety_level == "High":
                        st.error(f"**Anxiety Level:** {anxiety_level} (Confidence: {confidence:.2f})")
                        st.info("💡 **Tip:** It seems you are experiencing high anxiety. Try taking deep breaths, breaking your study material into small chunks, and getting enough sleep. Consider talking to a counselor if it persists.")
                    elif anxiety_level == "Medium":
                        st.warning(f"**Anxiety Level:** {anxiety_level} (Confidence: {confidence:.2f})")
                        st.info("💡 **Tip:** You have moderate anxiety. This is normal! Make sure you have a structured study plan and take regular breaks.")
                    else:
                        st.success(f"**Anxiety Level:** {anxiety_level} (Confidence: {confidence:.2f})")
                        st.info("💡 **Tip:** You seem calm and well-prepared. Keep up the good work and stay focused!")
                else:
                    st.error(f"Error from server: {response.text}")
                    
            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to the backend server. Please make sure the FastAPI backend is running on http://127.0.0.1:8000")
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")

st.markdown("---")
st.caption("Developed for GenAI Course Project")
