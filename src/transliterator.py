# src/transliterator.py
# Core Logic using Pytesseract (Tesseract OCR) and Indic-Transliteration

import pytesseract
from PIL import Image
import io
from indic_transliteration import sanscript, detect
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate

# --- FINAL FIX: Explicitly set the Tesseract command path for Streamlit Cloud ---
# This path is standard on the Debian-based servers used by Streamlit Cloud.
try:
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
except Exception:
    # Allows local testing to proceed if the system path is already correct
    pass

def detect_and_extract_text(image_bytes):
    """
    Uses Pytesseract to detect and extract text from an image, enabling Indic language support.
    """
    try:
        image = Image.open(io.BytesIO(image_bytes))
        
        # Use hin+eng language packs
        full_text = pytesseract.image_to_string(image, lang='hin+eng')

        return {
            "full_text": full_text.strip() if full_text else None,
            "lang_code": "Tesseract (hin+eng)" 
        }

    except pytesseract.TesseractNotFoundError:
        return {"full_text": None, "lang_code": "Tesseract not found (PATH error on server)."}
    except Exception as e:
        return {"full_text": None, "lang_code": f"Tesseract error: {e}"}


def transliterate_text(text, target_scheme):
    """
    Detects the source Indic script and transliterates the text to the target scheme.
    """
    try:
        source_scheme = detect.detect(text)

        # Fallback: If detection fails, assume Devanagari
        if source_scheme is None:
            source_scheme = sanscript.DEVANAGARI

        # Skip transliteration for Roman (English) text
        if source_scheme in [sanscript.HK, sanscript.IAST, sanscript.ITRANS]:
            return {
                "result": text,
                "source_script": "Roman (English)",
                "target_script": str(target_scheme),
                "error": None
            }

        # --- Perform transliteration ---
        transliterated_text = transliterate(
            data=text,
            _from=source_scheme,
            _to=target_scheme
        )

        return {
            "result": transliterated_text,
            "source_script": str(source_scheme),
            "target_script": str(target_scheme),
            "error": None
        }

    except Exception as e:
        return {
            "result": None,
            "source_script": None,
            "target_script": None,
            "error": f"Transliteration Error: {e}"
        }