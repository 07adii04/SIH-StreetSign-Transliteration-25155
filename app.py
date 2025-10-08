# app.py
# Streamlit UI for SIH PS 25155: Street Sign Transliteration Tool

import streamlit as st
import io
import requests
from streamlit_copy_button import copy_button
from src.transliterator import detect_and_extract_text, transliterate_text
from indic_transliteration import sanscript

# --- PAGE SETUP ---
st.set_page_config(page_title="Indic Transliteration Tool", page_icon="🛣️", layout="wide")

EXAMPLE_IMAGE_URL = "https://raw.githubusercontent.com/Ankit-Muran/Indian-Sign-Board-Datasets/main/Hindi/hi_10.jpeg"

# --- TITLE ---
st.title("Street Sign Transliteration Tool")
st.caption("Smart India Hackathon 25155 | OCR + Indic Transliteration")

with st.expander("ℹ️ About this Project"):
    st.write("""
        This tool extracts text from street sign images using **EasyOCR**
        and converts it into various Indic scripts using **indic-transliteration**.
        
         **Tech Stack:**
        - Python, Streamlit
        - EasyOCR (for multilingual OCR)
        - Indic Transliteration (for script conversion)
    """)

# --- LAYOUT ---
col1, col2 = st.columns(2)

# --- LEFT COLUMN: IMAGE INPUT ---
with col1:
    st.header("1️⃣ Upload Street Sign Image")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if st.button("📸 Try Example"):
        try:
            response = requests.get(EXAMPLE_IMAGE_URL, timeout=8)
            response.raise_for_status()
            uploaded_file = io.BytesIO(response.content)
            st.success("✅ Example loaded successfully!")
        except requests.exceptions.RequestException:
            st.error("⚠️ Failed to load example image.")

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

# --- RIGHT COLUMN: SCRIPT SELECTION ---
with col2:
    st.header("2️⃣ Select Target Script")

    scripts = {
        "Devanagari (देवनागरी)": sanscript.DEVANAGARI,
        "Bengali (বাংলা)": sanscript.BENGALI,
        "Gurmukhi (ਗੁਰਮੁਖੀ)": sanscript.GURMUKHI,
        "Gujarati (ગુજરાતી)": sanscript.GUJARATI,
        "Tamil (தமிழ்)": sanscript.TAMIL,
        "Telugu (తెలుగు)": sanscript.TELUGU,
    }

    target_script_name = st.selectbox("Convert to:", list(scripts.keys()))
    target_scheme = scripts[target_script_name]

    if uploaded_file:
        st.markdown("---")
        if st.button(" Run Transliteration", use_container_width=True, type="primary"):
            st.subheader(" Results")
            image_bytes = uploaded_file.getvalue()

            with st.spinner("Extracting text with EasyOCR..."):
                ocr_result = detect_and_extract_text(image_bytes)

            if ocr_result["full_text"]:
                st.success("✅ Text Extraction Successful")
                st.code(ocr_result["full_text"], language="text")

                with st.spinner(f"Transliterating to {target_script_name}..."):
                    trans_result = transliterate_text(ocr_result["full_text"], target_scheme)

                if trans_result["error"] is None:
                    st.success("✅ Transliteration Complete!")
                    st.code(trans_result["result"], language="text")
                    copy_button(trans_result["result"], "Copy Transliterated Text")
                else:
                    st.error(trans_result["error"])
            else:
                st.warning(ocr_result["lang_code"], icon="⚠️")
