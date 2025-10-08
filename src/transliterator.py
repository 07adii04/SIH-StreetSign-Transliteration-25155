# src/transliterator.py
import easyocr
from PIL import Image, UnidentifiedImageError
import io
from indic_transliteration import sanscript, detect
from indic_transliteration.sanscript import transliterate
import streamlit as st

# Lazily load the OCR reader only when needed; cache it for the life of the process.
@st.cache_resource(show_spinner=False)
def load_ocr_reader(languages=['en', 'hi']):
    """
    Load EasyOCR reader once and cache it.
    Keep languages small (en, hi, ...) to reduce model download size.
    """
    try:
        reader = easyocr.Reader(languages, gpu=False)
        return reader
    except Exception as e:
        # Return None — caller should handle this gracefully
        st.error(f"Failed to initialize EasyOCR reader: {e}")
        return None


def detect_and_extract_text(image_bytes):
    """
    Uses EasyOCR to extract text from an uploaded image.
    NOTE: This calls load_ocr_reader() lazily and will trigger model download on first use.
    """
    reader = load_ocr_reader()  # lazy, cached
    if reader is None:
        return {"full_text": None, "lang_code": "EasyOCR Initialization Failed"}

    try:
        image = Image.open(io.BytesIO(image_bytes))
        image.verify()
        image = Image.open(io.BytesIO(image_bytes))

        # Resize/thumbnail to speed OCR and reduce memory usage on large images
        max_dim = 1280
        if image.width > max_dim or image.height > max_dim:
            image.thumbnail((max_dim, max_dim))

        # paragraph=True merges lines which can be slower; keep it default if you want speed
        results = reader.readtext(image, detail=0, paragraph=True)
        full_text = "\n".join(results) if results else None

        return {
            "full_text": full_text.strip() if full_text else None,
            "lang_code": "EasyOCR (en, hi)"
        }

    except UnidentifiedImageError:
        return {"full_text": None, "lang_code": "Invalid File: Not a recognized image"}
    except Exception as e:
        return {"full_text": None, "lang_code": f"OCR Error: {e}"}


def transliterate_text(text, target_scheme):
    """Line-wise script detection + selective transliteration (keep English as-is)."""
    try:
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        processed = []
        for line in lines:
            try:
                src = detect.detect(line) or sanscript.DEVANAGARI
                if src in [
                    sanscript.DEVANAGARI, sanscript.TAMIL, sanscript.TELUGU,
                    sanscript.BENGALI, sanscript.GURMUKHI, sanscript.GUJARATI
                ]:
                    processed.append(transliterate(line, _from=src, _to=target_scheme))
                else:
                    processed.append(line)
            except Exception:
                processed.append(line)
        return {"result": "\n".join(processed), "error": None}
    except Exception as e:
        return {"result": None, "error": f"Transliteration Logic Error: {e}"}
