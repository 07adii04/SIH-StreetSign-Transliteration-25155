import streamlit as st
# Placeholder import for the logic file we will create in the next step
# from src.transliterator import detect_and_extract_text, transliterate_text 

# Set up the basic configuration for the page
st.set_page_config(
    page_title="SIH 25155 Transliteration Tool",
    layout="wide"
)

# --- Title and Project Info ---
st.title("🛣️ Transliterations Tool for Street Signs (SIH 25155)")
st.caption("Initial repository structure set up. Ready for implementation.")

# --- File Uploader Placeholder ---
st.header("1. Upload Street Sign Image")
uploaded_file = st.file_uploader(
    "Choose an image file...", 
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    # --- Processing Button Placeholder ---
    if st.button("Start Transliteration"):
        with st.spinner('Extracting text and performing transliteration...'):
            # Placeholder for future logic call
            st.success("Processing complete (Placeholder Result)")
            st.subheader("Transliterated Text (Output)")
            st.code("This is a placeholder result: The code will go here.", language="text")