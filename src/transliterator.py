# src/transliterator.py
# Core Logic: OCR (EasyOCR) + Transliteration (indic-transliteration)

import io
from PIL import Image
import numpy as np
import easyocr
from indic_transliteration import sanscript, detect
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate


def detect_and_extract_text(image_bytes):
    """
    Uses EasyOCR to extract text from uploaded street sign image.
    Supports Hindi + English for Indian signage.
    """
    try:
        reader = easyocr.Reader(['hi', 'en'], gpu=False)
        image = Image.open(io.BytesIO(image_bytes))
        result = reader.readtext(np.array(image), detail=0)
        full_text = " ".join(result)

        return {
            "full_text": full_text.strip() if full_text else None,
            "lang_code": "EasyOCR (hi+en)"
        }

    except Exception as e:
        return {"full_text": None, "lang_code": f"OCR Error: {e}"}


def transliterate_text(text, target_scheme):
    """
    Detects the source script and transliterates it into the target script.
    """
    try:
        if not text or not text.strip():
            return {
                "result": "",
                "source_script": None,
                "target_script": None,
                "error": "Empty text, nothing to transliterate."
            }

        source_scheme = detect.detect(text)

        if source_scheme in [sanscript.HK, sanscript.IAST]:
            return {
                "result": text,
                "source_script": "Roman (Latin / English)",
                "target_script": str(target_scheme),
                "error": None
            }

        transliterated_text = transliterate(
            data=text,
            sch_map=SchemeMap(SCHEMES[source_scheme], SCHEMES[target_scheme])
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
