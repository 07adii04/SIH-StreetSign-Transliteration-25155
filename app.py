# app.py
# Streamlit User Interface for SIH PS 25155: Street Sign Transliteration

import streamlit as st
# Import core functions from the logic file
from src.transliterator import detect_and_extract_text, transliterate_text 
# Import sanscript to access the language/script constants
from indic_transliteration import sanscript 

# --- Page Setup ---
st.set_page_config(
    page_title="SIH 25155 Transliteration Tool",
    layout="wide"
)

# --- Title and Project Info ---
st.title("🛣️ Transliterations Tool for Street Signs (SIH 25155)")
st.caption("Accurate, open-source script-to-script converter for multilingual Indic signage.")

# --- UI Layout: Side by Side ---
col1, col2 = st.columns([1, 1])

# --- Column 1: Image Upload ---
with col1:
    st.header("1. Upload Image")
    uploaded_file = st.file_uploader(
        "Choose an image file...", 
        type=["jpg", "jpeg", "png"]
    )
    
    # Display the uploaded image immediately
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', use_container_width=True)

# --- Column 2: Target Script Selection & Processing ---
with col2:
    st.header("2. Select Target Script")
    
    # Mapping user-friendly names to indic-transliteration constants
    script_options = {
        "Devanagari (देवनागरी)": sanscript.DEVANAGARI,
        "Telugu (తెలుగు)": sanscript.TELUGU,
        "Tamil (தமிழ்)": sanscript.TAMIL,
        "Bengali (বাংলা)": sanscript.BENGALI,
        "Gurmukhi (ਗੁਰਮੁਖੀ)": sanscript.GURMUKHI,
        "Gujarati (ગુજરાતી)": sanscript.GUJARATI,
    }
    target_script_name = st.selectbox(
        "Convert extracted text to which Indian script?",
        list(script_options.keys())
    )
    TARGET_SCHEME = script_options[target_script_name] 

    # --- Processing Button ---
    if uploaded_file is not None:
        st.markdown("---")
        if st.button("Start OCR and Transliteration", use_container_width=True, type="primary"):
            
            # Convert uploaded file (Streamlit object) to raw bytes for the OCR library
            image_bytes = uploaded_file.getvalue()
            
            st.subheader("Processing Results")
            
            # PHASE 1: OCR
            with st.spinner('Phase 1: Extracting text using EasyOCR (This may take a moment on first run)...'):
                ocr_result = detect_and_extract_text(image_bytes)
            
            if ocr_result["full_text"]:
                st.success("OCR Successful! Text Extracted.")
                
                # Show OCR metadata
                st.markdown(f"**OCR Engine:** `{ocr_result['lang_code']}`")
                st.markdown("### Extracted Text (Raw Output)")
                st.code(ocr_result["full_text"], language="text")
                
                # PHASE 2: Transliteration
                with st.spinner('Phase 2: Detecting source script and converting to target script...'):
                    # Call the transliteration function
                    trans_result = transliterate_text(ocr_result["full_text"], TARGET_SCHEME)

                if trans_result["error"] is None:
                    st.success("Transliteration Complete!")
                    
                    # Final Output Display
                    st.markdown(f"**Source Script Detected:** `{trans_result['source_script']}`")
                    st.markdown(f"**Target Script:** `{target_script_name}`")
                    
                    st.markdown("---")
                    st.markdown("### 🏆 Transliterated Result")