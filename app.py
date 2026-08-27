import streamlit as st
from groq import Groq
import urllib.parse
import base64

# 1. Cyber-Detective UI Configuration
st.set_page_config(page_title="MOGOJASTOR CLOUD TERMINAL", page_icon="🕵️‍♂️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #05060b; color: #f8f9fa; }
    h1 { color: #ff1f26; text-shadow: 0px 0px 20px #ff1f26; font-family: 'Consolas', monospace; font-weight: 800; }
    h3, label { color: #a2aab2; font-family: 'Consolas', monospace; }
    .stTextArea textarea { background-color: #0b0d16; color: #00ffcc; border: 2px solid #ff1f26; font-size: 16px; font-family: 'Consolas', monospace; }
    .stButton>button { background: linear-gradient(135deg, #7a0010, #ff1f26); color: #ffffff; border-radius: 4px; border: none; font-weight: bold; width: 100%; height: 55px; font-size: 18px; font-family: 'Consolas', monospace; box-shadow: 0 0 25px rgba(255,31,38,0.5); }
    .reasoning-box { background-color: #0b0d16; border-left: 6px solid #00ffcc; padding: 25px; border-radius: 4px; margin-top: 20px; font-size: 17px; line-height: 2.0; color: #ffffff; }
    .search-btn { display: inline-block; background-color: #121624; color: #00ffcc !important; border: 2px solid #00ffcc; padding: 12px 24px; border-radius: 4px; text-decoration: none; font-family: 'Consolas', monospace; font-weight: bold; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

st.title("🕵️‍♂️ MOGOJASTOR // CLOUD MAINFRAME")
st.subheader("CORE ENGINE STATUS: ACTIVE // SERVER LOCATION: PERMANENT CLOUD")

GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("SYSTEM FAULT: Groq API Key missing. Please configure secrets inside your Streamlit Cloud Dashboard.")
else:
    client = Groq(api_key=GROQ_API_KEY)

    col1, col2 = st.columns([1.2, 0.8])

    with col1:
        query = st.text_area("PASTE RIDDLE DATA MATRIX (ENGLISH/BANGLA):", placeholder="Enter text question...", height=180)
        uploaded_file = st.file_uploader("DROP TARGET SCREENSHOT OR LOGICAL DIAGRAM IMAGE:", type=["png", "jpg", "jpeg"])

    with col2:
        if uploaded_file is not None:
            st.image(uploaded_file, caption="IDENTIFIED VISUAL PARADIGM DATA", use_container_width=True)

    if st.button("RUN DEDUCTIVE WORKFLOW"):
        if query or uploaded_file:
            with st.spinner("Analyzing target constraints via Cloud Matrices..."):
                
                system_prompt = """
                You are 'Mogojastor', an analytical detective framework for the 'Feludagiri' competition based on Feluda Samagra.
                Give incredibly smart, logical, and deeply calculated answers to secure first place.
                
                STRICT PROTOCOL:
                1. You MUST write your entire response ONLY in the Bengali language (বাংলা ভাষা).
                2. Never provide shorthand, single-sentence, or trivial responses.
                3. Structure your output exactly within these three strict containers:
                
                ১. [গূঢ় পর্যবেক্ষণ (Critical Observation)]: Dissect hidden traps, riddle metaphors, wordplays, or visual parameters.
                ২. [যৌক্তিক বিশ্লেষণ (Logical Deduction Workflow)]: Provide step-by-step reasoning chains eliminating false outcomes.
                ৩. [চূড়ান্ত সমাধান (Verified Resolution)]: State the final, bulletproof solution.
                """
                
                try:
                    if uploaded_file is not None:
                        image_bytes = uploaded_file.getvalue()
                        base64_image = base64.b64encode(image_bytes).decode('utf-8')
                        
                        response = client.chat.completions.create(
                            model="llama-3.2-11b-vision-preview",
                            messages=[
                                {
                                    "role": "user",
                                    "content": [
                                        {"type": "text", "text": f"{system_prompt}\n\nQuestion text: {query}"},
                                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                                    ]
                                }
                            ]
                        )
                    else:
                        response = client.chat.completions.create(
                            model="llama-3.1-70b-versatile",
                            messages=[
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": query}
                            ]
                        )
                    
                    ai_output = response.choices.message.content
                    st.markdown("### 🧠 মগজাস্ত্র (Brainpower) বিশ্লেষণ ফলাফল:")
                    st.markdown(f'<div class="reasoning-box">{ai_output}</div>', unsafe_allow_html=True)
                    
                    search_query = query if query else "Feluda mystery logic riddle"
                    st.markdown(f'<a href="https://google.com{urllib.parse.quote_plus(search_query)}" target="_blank" class="search-btn">🌐 OPEN SEARCH ENGINE MATRIX</a>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Cloud Framework Protocol Fault: {e}")
        else:
            st.warning("Input arrays empty.")
