import streamlit as st
from src.transliterator import detect_and_extract_text, transliterate_text
from indic_transliteration import sanscript

# --- Streamlit Page Config ---
st.set_page_config(
    page_title="Street Sign Transliteration Tool",
    page_icon="🪧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- App Title and Description ---
st.title("🪧 Street Sign Transliteration Tool")
st.caption("A lightweight OCR + Transliteration web app built with Streamlit & EasyOCR.")

st.markdown("""
Upload an **image of a street sign**, and this tool will:
1. 🧠 Detect and extract text from the image using **EasyOCR**
2. 🔡 Automatically detect the script and transliterate it into your selected language
""")

# --- Sidebar for Configuration ---
st.sidebar.header("⚙️ Settings")

# Supported target transliteration schemes
TARGET_SCHEMES = {
    "English (IAST)": sanscript.ITRANS,
    "Devanagari (Hindi)": sanscript.DEVANAGARI,
    "Gujarati": sanscript.GUJARATI,
    "Tamil": sanscript.TAMIL,
    "Telugu": sanscript.TELUGU,
    "Bengali": sanscript.BENGALI,
    "Gurmukhi (Punjabi)": sanscript.GURMUKHI,
}

target_lang = st.sidebar.selectbox(
    "Select Target Script for Transliteration",
    list(TARGET_SCHEMES.keys())
)

st.sidebar.markdown("---")
st.sidebar.info("💡 Tip: The first OCR run may take ~1 minute (model download). Subsequent runs are instant!")

# --- File Uploader ---
uploaded_file = st.file_uploader("📸 Upload a Street Sign Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image_bytes = uploaded_file.read()

    # Display uploaded image preview
    st.image(image_bytes, caption="Uploaded Image", use_container_width=True)

    # --- Start Processing Button ---
    if st.button("🚀 Start Transliteration", type="primary"):
        st.info("Processing your image... Please wait ⏳")

        # Step 1: OCR Extraction (lazy-loaded, cached)
        with st.spinner("Initializing OCR model (first-time use may take 30–90s)..."):
            ocr_result = detect_and_extract_text(image_bytes)

        # Error handling
        if not ocr_result or not ocr_result.get("full_text"):
            st.error("❌ OCR failed or found no readable text in the image.")
        else:
            st.success("✅ Text extraction complete!")

            st.subheader("🧾 Extracted Text:")
            st.code(ocr_result["full_text"], language="text")

            # Step 2: Transliteration
            with st.spinner(f"Transliterating to {target_lang}..."):
                translit_result = transliterate_text(
                    ocr_result["full_text"],
                    TARGET_SCHEMES[target_lang]
                )

            if translit_result["error"]:
                st.error(f"⚠️ Transliteration failed: {translit_result['error']}")
            else:
                st.subheader(f"🌐 Transliterated Text ({target_lang}):")
                st.code(translit_result["result"], language="text")

                # Copy button (optional, if you added `streamlit-copy-button` in requirements)
                try:
                    from streamlit_copy_button import st_copy_button
                    st_copy_button(translit_result["result"])
                except Exception:
                    pass

else:
    st.warning("📤 Please upload an image to begin.")

# --- Footer ---
st.markdown("---")
st.caption(
    "Built by Aditya Tiwari | Powered by EasyOCR, Streamlit & Indic Transliteration Library"
)
