import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Study Coach", page_icon="📚")

# --- API key setup ---
# Locally: create a file called .env or .streamlit/secrets.toml (see below)
# On Streamlit Cloud: set this in Settings > Secrets as GEMINI_API_KEY = "..."
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-3.6-flash")

st.title("📚 Study Coach")
st.write("Tell me about your last study session and I'll give you honest, practical feedback.")

session_input = st.text_area(
    "What happened in your study session?",
    placeholder="e.g. studied circuits for 2 hours, kept getting distracted",
    height=100,
)

if st.button("Get feedback", type="primary"):
    if not session_input.strip():
        st.warning("Type something about your session first.")
    else:
        with st.spinner("Thinking..."):
            prompt = f"""You are a supportive but honest study coach.
A student just told you: "{session_input}"
Give them:
1. One honest observation about their session
2. One specific, doable suggestion for next time
3. A short focus tip for their next session
Keep it short and practical."""

            response = model.generate_content(prompt)
            st.markdown(response.text)

st.caption("Built with Streamlit + Gemini 3.6 Flash")
