import streamlit as st
import google.generativeai as genai

# Set your Gemini API Key (get one at https://ai.google.dev)
import streamlit as st
import google.generativeai as genai

# Load Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


st.set_page_config(page_title="🎭 AI Script Generator (Gemini Version)")

st.title("🎭 AI Script Generator - Gemini")
st.markdown("Enter your character setup and scene idea, and Gemini will generate an interactive dialogue between two characters.")

# User input
with st.form("generate_form"):
    prompt = st.text_area("✍️ Enter your setting (e.g. cold male lead + tsundere girl + high school first encounter)", height=150)
    submit = st.form_submit_button("✨ Generate Script")

# Initialize Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Generate dialogue
if submit and prompt.strip():
    with st.spinner("Gemini is generating the scene..."):
        try:
            response = model.generate_content(
                f"""You are an AI specialized in generating interactive anime-style story scripts. Based on the setting below, generate a short dialogue between two characters. Format it like this:
[Character Name]: "Dialogue"
[Character Name]: "Reply"

Setting: {prompt}
""")
            st.markdown("### 🎬 Generated Scene:")
            st.success(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
