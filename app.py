# app.py
# Streamlit UI for SIH PS 25155: Street Sign Transliteration Tool

import streamlit as st
import io
# Imports the core functions from your source code folder
from src.transliterator import detect_and_extract_text, transliterate_text
from indic_transliteration import sanscript

# --- Page Setup ---
st.set_page_config(
    page_title="Indic Transliteration Tool",
    page_icon="🛣️",
    layout="wide"
)

# --- Title ---
st.title("🛣️ Transliterations Tool for Street Signs (SIH 25155)")
st.caption("An open-source script converter for multilingual Indic signage.")

# --- Layout: 2 Columns for a cleaner look ---
col1, col2 = st.columns(2)

# --- Column 1: Image Upload and Display ---
with col1:
    st.header("1. Upload Image")
    uploaded_file = st.file_uploader(
        "Choose a street sign image...",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width="auto")
# --- Column 2: Script Selection & Processing ---
with col2:
    st.header("2. Select Target Script")

    # Dictionary mapping user-friendly names to library codes
    script_options = {
        "Telugu (తెలుగు)": sanscript.TELUGU,
        "Tamil (தமிழ்)": sanscript.TAMIL,
        "Bengali (বাংলা)": sanscript.BENGALI,
        "Gurmukhi (ਗੁਰਮੁਖੀ)": sanscript.GURMUKHI,
        "Gujarati (ગુજરાતી)": sanscript.GUJARATI,
        "Devanagari (देवनागरी)": sanscript.DEVANAGARI,
    }

    target_script_name = st.selectbox(
        "Convert the text to:",
        list(script_options.keys())
    )
    TARGET_SCHEME = script_options[target_script_name]

    if uploaded_file:
        st.markdown("---")
        # Main action button
        if st.button("🚀 Start Transliteration", use_container_width=True, type="primary"):
            st.subheader("Results")
            image_bytes = uploaded_file.getvalue()

            # --- PHASE 1: OCR ---
            with st.spinner("🔍 Phase 1: Extracting text using EasyOCR..."):
                ocr_result = detect_and_extract_text(image_bytes)

            if ocr_result["full_text"]:
                st.success("✅ OCR Successful!")
                st.markdown("#### Extracted Text (Source)")
                st.code(ocr_result["full_text"], language="text")

                # --- PHASE 2: Transliteration ---
                with st.spinner(f"🔤 Phase 2: Converting to {target_script_name}..."):
                    trans_result = transliterate_text(ocr_result["full_text"], TARGET_SCHEME)

                if trans_result["error"] is None:
                    st.success("✅ Transliteration Complete!")
                    st.markdown(f"#### Transliterated Text ({target_script_name})")
                    st.code(trans_result["result"], language="text")

                    # --- DOWNLOAD SECTION ---
                    st.markdown("---")
                    # TXT Download
                    st.download_button(
                        label="⬇️ Download as TXT",
                        data=trans_result["result"].encode("utf-8"),
                        file_name="transliteration_result.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                else:
                    st.error(f"Transliteration failed: {trans_result['error']}")
            else:
                st.error(f"OCR failed. The engine reported: {ocr_result['lang_code']}")