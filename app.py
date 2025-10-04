# app.py
# Streamlit User Interface

import streamlit as st
# 1. Import core function from your logic file
from src.transliterator import detect_and_extract_text 
# 2. Import sanscript to use the script constants for selection
from indic_transliteration import sanscript 

# --- Page Setup ---
st.set_page_config(
    page_title="SIH 25155 Transliteration Tool",
    layout="wide"
)

# --- Title and Project Info ---
st.title("🛣️ Transliterations Tool for Street Signs (SIH 25155)")
st.caption("A tool for accurate script-to-script conversion of Indic street signs.")

# --- File Uploader and Target Script Selection ---
col1, col2 = st.columns(2)

with col1:
    st.header("1. Upload Image")
    uploaded_file = st.file_uploader(
        "Choose an image file...", 
        type=["jpg", "jpeg", "png"]
    )

with col2:
    st.header("2. Select Target Script")
    # Mapping user-friendly names to sanscript constants
    script_options = {
        "Telugu (తెలుగు)": sanscript.TELUGU,
        "Bengali (বাংলা)": sanscript.BENGALI,
        "Devanagari (देवनागरी)": sanscript.DEVANAGARI,
        "Tamil (தமிழ்)": sanscript.TAMIL,
    }
    target_script_name = st.selectbox(
        "Convert to which Indian script?",
        list(script_options.keys())
    )
    TARGET_SCHEME = script_options[target_script_name] 


# --- Processing Logic ---
if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    if st.button("Start OCR and Transliteration", use_container_width=True):
        
        # Convert uploaded file (Streamlit object) to raw bytes for the Vision API
        image_bytes = uploaded_file.getvalue()
        
        st.subheader("Processing Results")
        
        with st.spinner('Phase 1: Extracting text (OCR) and detecting script...'):
            # CALL THE OCR FUNCTION
            ocr_result = detect_and_extract_text(image_bytes)
        
        # --- Display OCR Results ---
        if ocr_result["full_text"]:
            st.success("OCR Successful! Text Extracted.")
            
            st.markdown(f"**Detected Language Hint (from Google):** `{ocr_result['lang_code'] or 'N/A'}`")
            st.markdown("### Extracted Text (Raw OCR Output)")
            st.code(ocr_result["full_text"], language="text")
            
            # Placeholder for Phase C: Transliteration
            st.info("Transliteration logic (Phase C) will go here to convert the text above.")
            
        else:
            st.error("OCR Failed to extract text.")
            st.caption("Possible issues: Poor image quality, non-textual image, or **Google Cloud Credentials not correctly set**.")