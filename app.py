import streamlit as st
import requests
import random

# Page config
st.set_page_config(page_title="AI Monitor", page_icon="🌡️", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>🌡️ AI Smart Environment Monitor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Real-time AI-based environmental analysis</p>", unsafe_allow_html=True)

st.write("")

# Button centered
col1, col2, col3 = st.columns([1,2,1])
with col2:
    generate = st.button("🚀 Generate Data")

if generate:

    temperature = random.randint(25, 45)
    humidity = random.randint(40, 80)

    # Cards layout
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="🌡️ Temperature", value=f"{temperature} °C")

    with col2:
        st.metric(label="💧 Humidity", value=f"{humidity} %")

    st.write("")

    # AI Response Box
    st.markdown("### 🤖 AI Recommendation")

    prompt = f"""
    Temperature: {temperature}°C
    Humidity: {humidity}%
    Give short and practical advice in 2 lines.
    """

    with st.spinner("Analyzing data..."):
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        result = response.json()["response"]

    st.success(result)

    st.markdown("---")

# Footer
st.markdown(
    "<p style='text-align: center; color: gray;'>Built with ❤️ using Streamlit + Ollama</p>",
    unsafe_allow_html=True
)