# src/transliterator.py
# Core Logic using EasyOCR and Indic-Transliteration

import easyocr
from PIL import Image
import io
from indic_transliteration import sanscript, detect
from indic_transliteration.sanscript import transliterate

# This is a critical optimization:
# The EasyOCR reader is initialized only ONCE when the app starts.
# This avoids reloading the large model on every user interaction.
try:
    READER = easyocr.Reader(['en', 'hi'], gpu=False)
except Exception as e:
    # If initialization fails (e.g., on a resource-limited server),
    # the READER will be None, and we can handle it gracefully.
    print(f"Error initializing EasyOCR Reader: {e}")
    READER = None

def detect_and_extract_text(image_bytes):
    """Uses EasyOCR to extract all text from an image."""
    if READER is None:
        return {"full_text": None, "lang_code": "EasyOCR Engine Failed to Initialize"}

    try:
        image = Image.open(io.BytesIO(image_bytes))
        # detail=0 returns a list of strings, paragraph=True groups them.
        results = READER.readtext(image, detail=0, paragraph=True)
        full_text = "\n".join(results)
        
        return {
            "full_text": full_text.strip() if full_text else None,
            "lang_code": "EasyOCR (en, hi)"
        }
    except Exception as e:
        return {"full_text": None, "lang_code": f"OCR Runtime Error: {e}"}

def transliterate_text(text, target_scheme):
    """Detects the source script and transliterates it to the target script."""
    try:
        # Auto-detect the script of the extracted text
        source_scheme = detect.detect(text)
        # Default to Devanagari if detection is uncertain
        if source_scheme is None:
            source_scheme = sanscript.DEVANAGARI

        transliterated_text = transliterate(
            data=text,
            _from=source_scheme,
            _to=target_scheme
        )
        return {"result": transliterated_text, "error": None}
    except Exception as e:
        return {"result": None, "error": f"Transliteration Logic Error: {e}"}