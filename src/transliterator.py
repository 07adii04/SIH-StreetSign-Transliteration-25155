# src/transliterator.py
# Core Logic using EasyOCR and Indic-Transliteration

import easyocr
from PIL import Image, UnidentifiedImageError
import io
from indic_transliteration import sanscript, detect
from indic_transliteration.sanscript import transliterate
import streamlit as st

@st.cache_resource(show_spinner=False)
def load_ocr_reader():
    """Loads EasyOCR model only once using Streamlit cache."""
    try:
        reader = easyocr.Reader(['en', 'hi'], gpu=False)
        return reader
    except Exception as e:
        st.error(f"❌ Failed to initialize EasyOCR: {e}")
        return None

def detect_and_extract_text(image_bytes):
    """Uses EasyOCR to extract text from an uploaded image."""
    reader = load_ocr_reader()
    if reader is None:
        return {"full_text": None, "lang_code": "EasyOCR Engine Initialization Failed"}

    try:
        image = Image.open(io.BytesIO(image_bytes))
        image.verify()  # Check for file corruption
        image = Image.open(io.BytesIO(image_bytes))  # Reopen for processing
        
        results = reader.readtext(image, detail=0, paragraph=True)
        full_text = "\n".join(results)
        
        return {
            "full_text": full_text.strip() if full_text else None,
            "lang_code": "EasyOCR (en, hi)"
        }

    except UnidentifiedImageError:
        return {"full_text": None, "lang_code": "Invalid File: Not an image format."}
    except Exception as e:
        return {"full_text": None, "lang_code": f"OCR Error: {e}"}


def transliterate_text(text, target_scheme):
    """Detects script and transliterates it into the target script."""
    try:
        source_scheme = detect.detect(text) or sanscript.DEVANAGARI
        transliterated = transliterate(text, _from=source_scheme, _to=target_scheme)
        return {"result": transliterated, "error": None}
    except Exception as e:
        return {"result": None, "error": f"Transliteration Error: {e}"}
