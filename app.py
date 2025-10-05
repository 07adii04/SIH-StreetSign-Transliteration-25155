# app.py
# Streamlit UI for SIH PS 25155: Street Sign Transliteration Tool

import streamlit as st
import io
from src.transliterator import detect_and_extract_text, transliterate_text
from indic_transliteration import sanscript

# --- Page Setup ---
st.set_page_config(
    page_title="SIH 25155 Transliteration Tool",
    layout="wide"
)

# --- Title ---
st.title("🛣️ Transliterations Tool for Street Signs (SIH 25155)")
st.caption("Accurate, open-source script converter for multilingual Indic signage.")

# --- Layout: 2 Columns ---
col1, col2 = st.columns([1, 1])

# --- Column 1: Upload ---
with col1:
    st.header("1. Upload Image")
    uploaded_file = st.file_uploader(
        "Choose an image file...",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        # NOTE: Using use_container_width=True is correct, as requested by Streamlit warnings
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

# --- Column 2: Script Selection & Processing ---
with col2:
    st.header("2. Select Target Script")

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

    if uploaded_file:
        st.markdown("---")

        if st.button("🚀 Start OCR and Transliteration", use_container_width=True, type="primary"):
            st.subheader("Processing Results")

            image_bytes = uploaded_file.getvalue()

            # --- PHASE 1: OCR ---
            with st.spinner("🔍 Phase 1: Extracting text using Tesseract..."):
                ocr_result = detect_and_extract_text(image_bytes)

            if ocr_result["full_text"]:
                st.success("✅ OCR Successful!")
                st.markdown(f"**OCR Engine:** `{ocr_result['lang_code']}`")
                st.markdown("### Extracted Text")
                st.code(ocr_result["full_text"], language="text")

                # --- PHASE 2: Transliteration ---
                with st.spinner("🔤 Phase 2: Transliteration in progress..."):
                    trans_result = transliterate_text(ocr_result["full_text"], TARGET_SCHEME)

                if trans_result["error"] is None:
                    st.success("✅ Transliteration Complete!")
                    st.markdown(f"**Source Script:** `{trans_result['source_script']}`")
                    st.markdown(f"**Target Script:** `{target_script_name}`")

                    st.markdown("---")
                    st.markdown("### 🏆 Transliterated Result")
                    st.code(trans_result["result"], language="text")

                    # --- DOWNLOAD SECTION ---
                    # 1. TXT Download
                    txt_data = io.BytesIO(trans_result["result"].encode("utf-8"))
                    st.download_button(
                        label="⬇️ Download as TXT",
                        data=txt_data,
                        file_name="transliteration_result.txt",
                        mime="text/plain",
                        use_container_width=True
                    )

                    # 2. CSV Download
                    csv_data = io.BytesIO(("Extracted Text,Transliterated Text\n"
                                          f"\"{ocr_result['full_text'].replace('\"', '""')}\",\"{trans_result['result'].replace('\"', '""')}\"").encode("utf-8"))
                    st.download_button(
                        label="⬇️ Download as CSV",
                        data=csv_data,
                        file_name="transliteration_result.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
                else:
                    st.error(f"Transliteration failed: {trans_result['error']}")
            else:
                st.error(f"OCR failed: {ocr_result['lang_code']}")